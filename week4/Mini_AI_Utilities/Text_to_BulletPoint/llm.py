from openai import OpenAI
import os



client=OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def call_llm(meassages,model="llama-3.1-8b-instant"):
     try:
      response=client.chat.completions.create(
        model=model,
        messages=meassages,
        temperature=0.3
    )
      return response.choices[0].message.content
     
     except Exception as e:
        print("LLM ERROR:", e)
        return "call_llm not work"