# 🧠 Brightmind

**Brightmind** is an AI-powered mental health companion designed to support individuals experiencing anxiety and depression through real-time conversations—both voice and chat. Built with a deep focus on empathy, accessibility, and privacy, Brightmind uses cutting-edge LLMs and voice technologies to offer an always-available, judgment-free space.

---

## ✨ Features

- 🧘 **Real-time Voice Therapy** using Whisper (speech-to-text) and Croque (text-to-speech)
- 💬 **Conversational AI Chat** powered by large language models for responsive and emotionally intelligent dialogue
- 🧠 **Memory-Aware Conversations** with personalized context stored and retrieved using Pinecone vector DB
- 🧾 **Secure Chat History** stored in MongoDB with user-specific access and encryption
- 🎯 **Minimalist Frontend** for focused, distraction-free interaction using Next.js and Tailwind CSS
- ⚡ **FastAPI Backend** for real-time API handling and session management

---

## 🏗️ Tech Stack

| Layer       | Technology           |
|-------------|----------------------|
| Frontend    | Next.js, Tailwind CSS |
| Backend     | FastAPI              |
| Database    | MongoDB (user/session data), Pinecone (vector memory) |
| Audio       | Whisper (ASR), Croque TTS (Voice response) |
| AI Model    | OpenAI GPT / Custom LLM integration |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- MongoDB Atlas or local instance
- Pinecone API Key
- OpenAI API Key (or other LLM provider)
- Whisper & Croque setup

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/DhruvGorasiya/brightmind.git
cd brightmind
```

2. **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. **Frontend Setup**
```bash
cd frontend
npm install
```

### Environment Variables

1. **Backend (.env)**
```env
MONGODB_URI=your_mongodb_uri
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_key
```

2. **Frontend (.env.local)**
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

### Running the Application

1. **Start the Backend**
```bash
cd backend
uvicorn main:app --reload
```

2. **Start the Frontend**
```bash
cd frontend
npm run dev
```

## 📁 Project Structure

```

## 🔒 Privacy & Security

- All user data is encrypted at rest and in transit
- Conversations are stored securely in MongoDB with user-specific access
- No data is shared with third parties
- Regular security audits and updates

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- OpenAI for GPT integration
- MongoDB for database services
- Pinecone for vector storage
- Next.js team for the amazing framework
- All contributors and supporters of the project

---

"Mental health support should be accessible, empathetic, and always available. Brightmind is a small step toward that future." 🌱