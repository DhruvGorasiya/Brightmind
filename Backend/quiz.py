import openai

def generate_quiz(topic: str, difficulty: str = "medium") -> str:
    prompt = f"""
Create a {difficulty} level 5-question multiple choice quiz about {topic}.
Each question must have 4 options, and clearly mark the correct answer.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    quiz = response["choices"][0]["message"]["content"].strip()
    return quiz