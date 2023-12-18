# https://fastapi.tiangolo.com/tutorial/first-steps/
# run: uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()


#from fastapi.staticfiles import StaticFiles
#app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return {"Hello": "World"}


from typing import Union
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

import pandas as pd
import json

_testdata = 'static/SHARADAR-ACTIONS.csv'

@app.get("/table")
async def read_table():
    df = pd.read_csv(_testdata)
    #return df.to_json(orient='values', date_format='iso', indent=2)
    return json.dumps(json.loads(df.to_json(orient='split', date_format='iso')))
    #return df.to_json(orient='records', date_format='iso', lines=True)

import csv

@app.get("/csv")
async def read_csv():
    data = []
    with open(_testdata, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    #return json.dumps(data) # displayed quoted str with embedded and escaped quotes
    return data # displayed as list of lists of strings
    
