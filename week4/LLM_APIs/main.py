from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

from llm import call_llm
from prompts import (
    summarization_prompt,
    rewriting_prompt,
    classification_prompt,
    keyword_prompt
)
from storage import store_record

app = FastAPI()

class TextRequest(BaseModel):
    text: str


@app.post("/summarize")
def summarize(req: TextRequest):
    prompt = summarization_prompt(req.text)
    result = call_llm(prompt)

    store_record("summarization", prompt, result)
    return {"summary": result}

@app.post("/rewrite")
def rewrite(req: TextRequest):
    prompt = rewriting_prompt(req.text)
    result = call_llm(prompt)

    store_record("rewriting", prompt, result)
    return {"rewritten_text": result}


@app.post("/classify")
def classify(req: TextRequest):
    prompt = classification_prompt(req.text)
    result = call_llm(prompt)

    store_record("classification", prompt, result)
    return {"classification": result}


   

@app.post("/keywords")
async def extract_keywords(req: TextRequest):
    try:
        prompt = keyword_prompt(req.text)
        result = call_llm(prompt)
        store_record("keyword_extraction", req.text, result)
        return {"keywords": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

