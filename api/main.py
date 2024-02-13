from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import DataBase

#create app
app = FastAPI()

app.db = DataBase()

class Food(BaseModel):
    name: str
    recipe: str
    
#defind routes
@app.get('/')
def hello():
    return {"hello": "food lover!"}

#get food from db
@app.get('/food')
def get_food():
    return app.db.all()

#get specific food from db
@app.get('/food/{food_name}')
def get_specific_food(food_name: str):
    try:
        return app.db.get(food_name)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Food item '{food_name}' not found.")

#creat food from db
@app.post('/food')
def create_food(food: Food):
    app.db.put(food.name, food.model_dump()) #use model_dump instead of dict()
    return app.db.get(food.name)

#delet food from db
@app.delete('/food/{food_name}') 
def delete_food(food_name: str):
    try:
        app.db.delete(food_name)
        return {"detail": f"Food item '{food_name}' deleted."}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Food item '{food_name}' not found.")