class Node():
    def __init__(self, id, value):
        self._id = id
        self._value = value
    
    def get_id(self):
        return self._id
    
    def get_value(self):
        return self._value