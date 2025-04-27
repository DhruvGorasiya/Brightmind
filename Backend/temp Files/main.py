from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from openai import OpenAI
import os
from datetime import datetime
from langchain.vectorstores.pinecone import Pinecone as LangchainPinecone
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader    
import glob

from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_7UFomm_Kecd55P2SgC2oYEWxT1tpZ6Rj3Y4ZajpZ458Xx9jgKU6qucGLEhWmp2ekKdqALY")

index = pc.Index("brightmind")

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI()

client.api_key = os.getenv("OPENAI_API_KEY")

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    message: str
    timestamp: datetime

@app.post("/api/ai_message", response_model=MessageResponse)
async def handle_message(request: MessageRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant, who specializes in helping people with their mental health."},
                {"role": "user", "content": request.message}
            ],
            max_tokens=500,
            temperature=0.7,
        )

        ai_response = response.choices[0].message.content

        return MessageResponse(
            message=ai_response,
            timestamp=datetime.now()
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)