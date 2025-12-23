from fastapi import FastAPI

from llm import call_llm
from prompt import sentimental_prompt
from record_storage import store_record

app= FastAPI()



@app.post("/analyze")
def main():
    print("=== Sentiment Analysis CLI ===")
    text=input("Enter the text:")

    if not text.strip():
        print("No text entered.")
        return

    prompt=sentimental_prompt(text)
    try:
     sentiment=call_llm( prompt)
     store_record("sentimantal analysis", prompt, sentiment)
     print("\nResult:")
     print(f"Text: {text}")
     print(f"Sentiment: {sentiment}")
    except Exception:
     store_record("sentimantal analysis", prompt, sentiment)
     print("\n AI service is busy. Please try again in a few seconds.")
 

if __name__ == "__main__":
    main()