"use client";

import { useState } from "react";
import { Send } from "lucide-react";
import axios from "axios";

interface Message {
  role: "user" | "assistant";
  content: string;
  timestamp: Date;
}

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage: Message = {
      role: "user",
      content: input.trim(),
      timestamp: new Date(),
    };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const { data } = await axios.post("/api/chat", {
        message: input.trim(),
      });
      const aiMessage: Message = {
        role: "assistant",
        content: data.message,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error("Failed to send message:", error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-50 dark:bg-gray-900">
      {/* Header */}
      <div className="bg-white dark:bg-gray-800 border-b dark:border-gray-700 p-4 shadow-sm">
        <div className="max-w-3xl mx-auto flex items-center justify-center">
          <h1 className="text-xl font-semibold text-gray-800 dark:text-white">
            Chat with AI Assistant
          </h1>
        </div>
      </div>

      {/* Chat container */}
      <div className="flex-1 overflow-hidden">
        <div className="max-w-3xl h-full mx-auto flex flex-col">
          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {messages.length === 0 && (
              <div className="text-center text-gray-500 dark:text-gray-400 mt-8">
                Start a conversation by sending a message below.
              </div>
            )}

            {messages.map((message, index) => (
              <div
                key={index}
                className={`flex ${
                  message.role === "user" ? "justify-end" : "justify-start"
                }`}
              >
                <div
                  className={`
                    max-w-[80%] px-4 py-2 rounded-2xl shadow-sm
                    ${
                      message.role === "user"
                        ? "bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-br-none"
                        : "bg-white dark:bg-gray-800 rounded-bl-none border dark:border-gray-700"
                    }
                  `}
                >
                  <div
                    className={`text-sm ${
                      message.role === "user"
                        ? "text-white"
                        : "text-gray-800 dark:text-gray-200"
                    }`}
                  >
                    {message.content}
                  </div>
                  <div
                    className={`text-xs mt-1 ${
                      message.role === "user"
                        ? "text-blue-200"
                        : "text-gray-500"
                    }`}
                  >
                    {message.timestamp.toLocaleTimeString([], {
                      hour: "2-digit",
                      minute: "2-digit",
                    })}
                  </div>
                </div>
              </div>
            ))}

            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-white dark:bg-gray-800 px-4 py-2 rounded-2xl rounded-bl-none border dark:border-gray-700">
                  <span className="text-gray-400 dark:text-gray-500 animate-pulse">
                    Typing...
                  </span>
                </div>
              </div>
            )}
          </div>

          {/* Input form */}
          <div className="p-4 bg-white dark:bg-gray-800 border-t dark:border-gray-700">
            <form
              onSubmit={handleSubmit}
              className="max-w-3xl mx-auto flex items-center gap-2 relative"
            >
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type your message..."
                className="flex-1 p-3 pl-12 bg-gray-100 dark:bg-gray-900 border dark:border-gray-700 rounded-full shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-600 dark:text-white transition-all"
                disabled={isLoading}
              />
              <button
                type="submit"
                disabled={isLoading}
                className="absolute left-4 top-1/2 transform -translate-y-1/2 p-2 text-gray-500 dark:text-gray-400 hover:text-blue-500 dark:hover:text-blue-400 transition-colors"
              >
                <Send className="w-5 h-5" />
              </button>
              <button
                type="submit"
                disabled={isLoading}
                className="p-3 bg-blue-600 text-white rounded-full hover:bg-blue-700 disabled:opacity-50 disabled:hover:bg-blue-600 transition-colors"
              >
                <Send className="w-5 h-5" />
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
