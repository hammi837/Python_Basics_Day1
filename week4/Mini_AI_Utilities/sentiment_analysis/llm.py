from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def call_llm(messages):
    try:
        # Convert chat messages into a single prompt
        prompt = ""
        for msg in messages:
            prompt += msg["content"] + "\n"

            response = client.models.generate_content(
              model="gemini-2.5-flash",
              contents=prompt)

        return response.text.strip()

    except Exception as e:
        print("LLM ERROR:", e)
        return "call_llm not work"
