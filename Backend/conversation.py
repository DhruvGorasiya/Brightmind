from datetime import datetime

class ConversationManager:
    def __init__(self):
        self.conversations = {}

    def add_message(self, user_id, question, answer):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "question": question,
            "answer": answer
        }
        if user_id not in self.conversations:
            self.conversations[user_id] = []
        self.conversations[user_id].append(entry)

    def get_conversation(self, user_id):
        return self.conversations.get(user_id, [])