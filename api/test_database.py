from database import DataBase

def test_get():
    db = DataBase()
    db._data = {"key": "value"}

    result = db.get("key")

    assert result == "value"

def test_put():
    db = DataBase()

    db.put("some_key", "some_value")

    assert db._data["some_key"] == "some_value"

def test_all():
    db = DataBase()
    dict_of_data = {"key": "value", "some_key": "some_value"}
    db._data = dict_of_data

    result = db.all()

    assert result == dict_of_data

def test_delete():
    db = DataBase()
    db.put("key_to_delete", "value")
    assert "key_to_delete" in db.all()
    db.delete("key_to_delete")
    assert "key_to_delete" not in db.all()
    try:
        db.delete("non_existent_key")
        assert False, "KeyError was not raised"
    except KeyError:
        assert True
