from openai import OpenAI
import os
import uuid
from typing import Optional
from pinecone import Pinecone, ServerlessSpec
import ast

pc = Pinecone(api_key="PINECONE_API_KEY")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI()

client.api_key = OPENAI_API_KEY

index = pc.Index("chatapp")

counter = 1

print(index)

def fetch_conversation_by_namespace(namespace_name):
    query_response = index.query(
        vector=[0] * 1536,
        top_k=10000,
        namespace=namespace_name,
        include_metadata=True
    )
    
    conversations = {}
    for match in query_response.matches:
        print(match)
        # conversations[match.id] = ast.literal_eval(match.metadata['full_text'])
    
    return conversations

def generate_namespace_id():
    stats = index.describe_index_stats()
    existing_namespaces = stats.namespaces.keys()
    next_num = 1
    
    for namespace in existing_namespaces:
        if namespace.startswith('chatapp'):
            try:
                num = int(namespace.replace('chatapp', ''))
                next_num = max(next_num, num + 1)
            except ValueError:
                continue
    
    return next_num

def embed_conversation(conversation_text):
    conversation_id = str(uuid.uuid4())
    
    _conversation_text = conversation_text.split("user:")
    
    _conversation_text_list = [msg.split("assistant:") for msg in _conversation_text[1:]]
    
    conversation_dict = {}
    for i,msg in enumerate(_conversation_text_list):
        conversation_dict[f"user_{i}"], conversation_dict[f"assistant_{i}"] = msg[0], msg[1]
    
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=conversation_text
    )
    embedding = response.data[0].embedding
    
    index.upsert(
        vectors=[{
            'id': conversation_id,
            'values': embedding,
            'metadata': {
                'full_text': str(conversation_dict)
            }
        }],
        namespace="chatapp"
    )
    
    return conversation_id

def chatbot(prompt,topic, prev_convo: Optional):
    try:
        if prev_convo:  
            system_context = f"You are a helpful assistant that specializes in {topic}. Please only answer questions related to {topic}. If the question is not related to {topic}, politely redirect the user to ask about {topic} instead. and this is the previous conversation of the user: {prev_convo}, based on this conversation, answer the next questions."
        else:
            system_context = f"You are a helpful assistant that specializes in {topic}. Please only answer questions related to {topic}. If the question is not related to {topic}, politely redirect the user to ask about {topic} instead."

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_context},
                {"role": "user", "content": prompt},
            ],
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
    
    
def fetch_conversation(conversation_id):
    result = index.fetch(ids=[conversation_id], namespace="chatapp2")
    return result.vectors[conversation_id].metadata['full_text']

def main():

    conversation = []
    
    stats = index.describe_index_stats()
    namespaces = stats.namespaces
    
    for namespace_id in namespaces.keys():
        query_response = index.query(
            vector=[0] * 1536,
            top_k=10000,
            namespace=namespace_id,
            include_metadata=True
        )
        
        for match in query_response.matches:
            print(f"Conversation ID: {match.id}")
        
    stats = index.describe_index_stats()
    existing_namespaces = stats.namespaces.keys()
    
    conversations = fetch_conversation_by_namespace("chatapp2")
    print(conversations)

    for conv_id, conv_content in conversations.items():
        print(f"Conversation ID: {conv_id}")
        print(f"Content: {conv_content}")
        print("---")
    
    
    print(fetch_conversation("031014f4-707a-416e-90d9-10887fe2cf0d"))
    
    print(len(existing_namespaces))    

    print("Chatbot: Hello! How can I help you today? (Type 'exit' or 'quit' to end)")

    topic = input("Tell me the topic you want to have a chat about: ")

    print(f"Sure you can ask me anything about {topic}")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        response = chatbot(user_input,topic, conversation)
        print("Chatbot:", response)
        conversation.append({"role": "user", "content": user_input})
        conversation.append({"role": "assistant", "content": response})
        
    conversation_text = " ".join([f"{msg['role']}: {msg['content']}" for msg in conversation])

    conversation_id = embed_conversation(conversation_text)

    print("Conversation saved with ID:", conversation_id)
    
    print("Do you want to fetch a previous conversation? (y/n)")
    fetch_prev = input("Enter your choice: (y/n)")
    if fetch_prev.lower() == "y":
        conversation_id = input("Enter the conversation ID: ")
        conversation = fetch_conversation(conversation_id)
        print("Conversation:", conversation)

if __name__ == "__main__":
    main()
