import random

class TutorAgent:
    def __init__(self):
        self.actions = ["give_hint", "ask_clarifying_question", "full_answer"]
        self.probabilities = [0.15, 0.25, 0.6]

    def decide_action(self):
        """Decide the next action based on dynamic probabilities (RL simulation)."""
        action = random.choices(self.actions, self.probabilities)[0]
        return action

# Singleton instance
agent = TutorAgent()

def decide_action():
    return agent.decide_action()