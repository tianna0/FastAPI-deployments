class DataBase():
    def __init__(self):
        self._data = {}

    def get(self, key):
        if key in self._data:
            return self._data[key]
        raise KeyError
    
    def put(self, key, value):
        self._data[key] = value
    
    def all(self):
        return self._data
    
    def delete(self, key):
        if key in self._data:
            del self._data[key]
        else:
            raise KeyError