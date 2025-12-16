from fastapi  import FastAPI 

from pydantic import BaseModel
from typing import List

app = FastAPI()


class Contactbook(BaseModel):   #inherit basemodel   (/ ")
    id: int
    name: str
    phone_no: str

contact: List[Contactbook] =[]

@app.get("/")
def show_root():
    return {"message": "welocome to contact book"}

@app.get("/contact")
def get_contact():
    return contact

@app.post("/contact")
def add_contact(contacts: Contactbook ):
    contact.append(contacts)

@app.put("/contact/{contact_id}")
def update_contact(contact_id: int ,updated_value: Contactbook ):
      for index , contacts in enumerate(contact):
          if contacts.id==contact_id:
              contact[index]= updated_value
              return updated_value
          
      return {"error": "id not found"}


@app.delete("/contact/{contact_id}")
def del_contact(contact_id: int ):
    for index , contacts in enumerate(contact):
          if contacts.id==contact_id:
              delete=contact.pop(index)
              return delete

    return {"error": "id not found"}







    




