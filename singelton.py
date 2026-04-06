class PersonFactory:
    """PersonFactory"""
    def __init__(self):
        self._next_id = 1

    def create_person(self, name):
        person = Person(self._next_id, name)
        self._next_id += 1
        return person


class Person:
    """Person"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Database:
    _instance = None
 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

def create_db():
    return Database()
    
def is_singleton(factory):
    obj1 = factory()
    obj2 = factory()
    return obj1 is obj2


print(is_singleton(create_db))
