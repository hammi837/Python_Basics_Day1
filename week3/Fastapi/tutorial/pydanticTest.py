from pydantic import BaseModel
from datetime import datetime
from typing import *

class User(BaseModel):   # (/ ")
    id: int
    name: str ="hammad hafeez"
    signup_ts: datetime | None = None
    friend : list[int] =[]


external_data={

"id":"1",
"signup_ts":"2025-12-09 01:30",
"friend": [1,2,3]

}
user=User(**external_data)
print(user)
print(user.id)


