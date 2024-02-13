from fastapi.testclient import TestClient
from main import app
from database import DataBase

client = TestClient(app)

def setup_function(function):
    app.db = DataBase()

def test_hello():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"hello": "food lover!"}

def test_get_all_food_empty():
    response = client.get('/food')
    assert response.status_code == 200
    assert response.json() == {}

def test_create_food():
    food_item = {"name": "sandwich", "recipe": "bread, ham, cheese"}
    response = client.post('/food', json=food_item)
    assert response.status_code == 200
    assert response.json() == food_item

def test_get_all_food_with_data():
    app.db.put("sandwich", {"name": "sandwich", "recipe": "bread, ham, cheese"})
    response = client.get('/food')
    assert response.status_code == 200
    assert response.json() == {"sandwich": {"name": "sandwich", "recipe": "bread, ham, cheese"}}

def test_get_specific_food():
    app.db.put("sandwich", {"name": "sandwich", "recipe": "bread, ham, cheese"})
    response = client.get('/food/sandwich')
    assert response.status_code == 200
    assert response.json() == {"name": "sandwich", "recipe": "bread, ham, cheese"}

def test_get_specific_food_not_found():
    response = client.get('/food/not_a_sandwich')
    assert response.status_code == 404
    assert response.json() == {"detail": "Food item 'not_a_sandwich' not found."}

def test_delete_food():
    app.db.put("sandwich", {"name": "sandwich", "recipe": "bread, ham, cheese"})
    response = client.delete('/food/sandwich')
    assert response.status_code == 200
    assert response.json() == {"detail": "Food item 'sandwich' deleted."}

def test_delete_food_not_found():
    response = client.delete('/food/not_a_sandwich')
    assert response.status_code == 404
    assert response.json() == {"detail": "Food item 'not_a_sandwich' not found."}