class Contact():
    def __init__(self, name, phone_number) -> None:
        self._name = name
        self._phone_number = phone_number
        
        def get_name(self):
            return self._name
        def get_phone_number(self):
            return self._phone_number
        
        def set_name(self, new_name):
            self._name = new_name
        
        def set_phone_number(self, new_phone_number):
            self._phone_number = new_phone_number