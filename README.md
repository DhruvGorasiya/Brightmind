# Adaptive AI Tutor Backend

An intelligent, cloud-ready backend that powers an adaptive tutoring system using Reinforcement Learning (RL), Retrieval-Augmented Generation (RAG), LangChain, Pinecone vector database, and OpenAI's GPT-4.

Built with FastAPI, this backend enables personalized tutoring, quiz generation, and content adaptation — simulating a human-like, context-aware AI tutor.

---

## 🚀 Features

- **Adaptive Tutoring System** using RL-based decision making (hint, clarifying question, full answer)
- **RAG Pipeline**: Retrieve context from vector embeddings (Pinecone) to enhance GPT-4 responses
- **Conversation Memory**: Track and store student conversations with timestamps
- **Custom Quiz Generation**: Create topic-specific quizzes with difficulty settings (easy, medium, hard)
- **Personalized Learning Content**: Generate custom modules tailored to student's level (beginner, intermediate, advanced)
- **Scalable Cloud Architecture**: Deployable with Docker, GCP Cloud Run, AWS, etc.

---

## 🛠 Tech Stack

- **Backend Framework**: FastAPI
- **LLM**: OpenAI GPT-4
- **Vector Store**: Pinecone (via LangChain)
- **Prompt Engineering**: LangChain templates
- **Deployment Ready**: Docker + GCP
- **Logging**: Python standard logging
- **Memory Management**: In-memory conversation storage (can extend to DB)

---

## 🧩 Project Structure

```plaintext
adaptive_tutor_backend/
├── main.py               # API Server
├── agent.py              # Reinforcement Learning Agent
├── retriever.py          # Context Retriever via Pinecone
├── conversation.py       # Manage chat memory
├── quiz_generator.py     # Generate quizzes
├── content_generator.py  # Generate personalized content
├── requirements.txt      # Dependencies
├── README.md             # Project Overview (this file)
```

---

## 📦 Setup Instructions

1. **Clone the repository**
    ```sh
    git clone https://github.com/your-username/adaptive-tutor-backend.git
    cd adaptive-tutor-backend
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set environment variables**
    ```sh
    export OPENAI_API_KEY="your-openai-api-key"
    ```

4. **Run the FastAPI server**
    ```sh
    uvicorn main:app --reload
    ```

The API will be live at:  
http://127.0.0.1:8000

---

## 🔥 API Overview

### 1. Chat with Tutor

**POST** `/ask`

**Request:**
```json
{
  "user_id": "student123",
  "question": "What is the Pythagorean theorem?"
}
```

**Response:**
```json
{
  "answer": "The Pythagorean theorem states...",
  "action": "full_answer"
}
```

---

### 2. Generate Quiz

**POST** `/quiz`

**Request:**
```json
{
  "topic": "Machine Learning",
  "difficulty": "medium"
}
```

**Response:**
```json
{
  "quiz": "1. What is supervised learning? (a)..."
}
```

---

### 3. Generate Personalized Learning Content

**POST** `/personalized_content`

**Request:**
```json
{
  "topic": "Neural Networks",
  "level": "beginner"
}
```

**Response:**
```json
{
  "content": "Neural networks are computing systems inspired by..."
}
```

---

### 4. Retrieve Conversation History

**GET** `/conversation/{user_id}`

**Example:**
```
GET /conversation/student123
```

**Response:**
```json
{
  "conversation_history": [
    {
      "timestamp": "2025-04-27T14:02:22.202Z",
      "question": "What is AI?",
      "answer": "Artificial Intelligence is..."
    }
  ]
}
```