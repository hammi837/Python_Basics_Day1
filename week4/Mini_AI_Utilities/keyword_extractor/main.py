from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

from llm import call_llm
from prompt import keyword_prompt

from record_storage import store_record

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/keywords")
async def extract_keywords(req: TextRequest):
    try:
        prompt = keyword_prompt(req.text)
        result = call_llm(prompt)
        store_record("keyword_extraction", req.text, result)
        return {"keywords": result}
    except Exception as e:
        store_record("keyword_extraction", req.text, result)
        raise HTTPException(status_code=500, detail=str(e))