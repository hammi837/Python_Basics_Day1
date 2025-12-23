import json
from datetime import datetime


def store_record(task,prompt,response):
    record={

       "timestamp": datetime.utcnow().isoformat(),
       "task":task,
       "prompt":prompt,
       "response":response
    }

    with open("record.jsonl","a") as f:
        f.write(json.dumps(record) + "\n")
