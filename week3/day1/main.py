from fastapi  import FastAPI ,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from  pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
conn= MongoClient("mongodb+srv://Hlo_me123:zZMYFuKt5EftdKzU@notes.9vism0d.mongodb.net")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request ):
    docs=conn.notes.user1.find_one({})
    print(docs)
    newDocs=[]
    for doc in docs:
        docs.append(
            {
                "id": doc["_id"],
                "notes": doc["notes"]
            }
        )

    return templates.TemplateResponse(
        "index.html",{"request":request,"newDocs":newDocs}
    )
    












    




