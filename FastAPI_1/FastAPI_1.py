from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import os
from pydantic import BaseModel
   
# To run the sever   python -m uvicorn FastAPI_1:app --reload



app = FastAPI()

##FILE_PATH = r"C:\Users\esthe\OneDrive\Desktop\task 3\Task\Data\iris.json"
FILE_PATH ="FastAPI_1\iris.json"

# Helper function to read existing data
def read_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Helper function to append new payload
def append_data(payload:dict):
    data = read_data()
    data.append(payload)
    with open(FILE_PATH, "w") as f:
        json.dump(data, f ,indent=2)



class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    variety: str
    

@app.post("/append")
async def append_payload(payload: Iris):
    ##payload = await request.json()  # JSON מגיע כ-dict
    append_data(payload.dict())            # פשוט מוסיפים למערך
    return JSONResponse(content={"message": "Payload appended successfully"})


# @app.post("/append")
# async def append_payload(request: Request):
#     payload = await request.json()
#     append_data(payload)
#     return JSONResponse(content={"message": "Payload appended successfully"})



@app.get("/last10")
async def get_last_10():
    data = read_data()
    last_10 = data[-10:]  # get last 10 items
    return JSONResponse(content=last_10)

