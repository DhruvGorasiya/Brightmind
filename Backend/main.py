from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import openai
from agent import decide_action
from retriever import retrieve_context
from conversation import ConversationManager
from quiz_generator import generate_quiz
from content_generator import generate_personalized_content
import os
import logging

# Initialize app and logging
app = FastAPI(title="Adaptive AI Tutor Backend", version="2.0")
logging.basicConfig(level=logging.INFO)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Instantiate conversation manager
conversation_manager = ConversationManager()

# Request Models
class QueryRequest(BaseModel):
    user_id: str
    question: str

class ContentRequest(BaseModel):
    topic: str
    level: str = "beginner"

class QuizRequest(BaseModel):
    topic: str
    difficulty: str = "medium"

@app.get("/")
async def root():
    return {"message": "Adaptive Tutor Backend is running successfully!"}

@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        logging.info(f"Received question from user {request.user_id}: {request.question}")
        context = retrieve_context(request.question)
        action = decide_action()

        if action == "give_hint":
            context += "\n\nHint: Focus on key concepts."
        elif action == "ask_clarifying_question":
            context += "\n\nAsk back: Can you clarify your confusion?"

        prompt = f"""
You are an expert AI tutor. 
Use the context below to help the student.
Context: {context}
Student Question: {request.question}
Instruction ({action}): Formulate the best response.
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        answer = response["choices"][0]["message"]["content"].strip()
        conversation_manager.add_message(request.user_id, request.question, answer)

        return {"answer": answer, "action": action}

    except Exception as e:
        logging.error(f"Error processing question: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/quiz")
async def create_quiz(request: QuizRequest):
    try:
        quiz = generate_quiz(request.topic, request.difficulty)
        return {"quiz": quiz}
    except Exception as e:
        logging.error(f"Error creating quiz: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/personalized_content")
async def create_personalized_content(request: ContentRequest):
    try:
        content = generate_personalized_content(request.topic, request.level)
        return {"content": content}
    except Exception as e:
        logging.error(f"Error generating content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/conversation/{user_id}")
async def get_conversation(user_id: str):
    try:
        history = conversation_manager.get_conversation(user_id)
        return {"conversation_history": history}
    except Exception as e:
        logging.error(f"Error fetching conversation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))