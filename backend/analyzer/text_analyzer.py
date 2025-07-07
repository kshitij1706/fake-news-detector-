from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text(text):
    prompt = f"Check the factual accuracy of the following statement. Provide a short explanation.\n\nText: {text}"
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    answer = response['choices'][0]['message']['content']
    return 0.8, answer  # Placeholder score
