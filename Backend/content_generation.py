import openai

def generate_personalized_content(topic: str, level: str = "beginner") -> str:
    prompt = f"""
Create a personalized learning module about {topic}.
Target it for a {level} learner.
Organize it into clear sections with examples and short exercises.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["choices"][0]["message"]["content"].strip()
    return content