from fastapi import FastAPI
from pydantic import BaseModel
from prompt import BulletPoint_prompt
from llm import call_llm
from record_storage import store_record
app=FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/BulletPoint")
def text_converter(req: TextRequest):
    try:
     prompt= BulletPoint_prompt(req.text)
     result= call_llm(prompt)
     store_record("text_converter", prompt, result)
     return {"bullet_point text:": result}
    except Exception:
     store_record("text_converter", prompt, result)
     print("\n AI service is busy. Please try again in a few seconds.")
     