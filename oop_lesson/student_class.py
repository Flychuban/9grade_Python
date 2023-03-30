class Student:
    def __init__(self, number, name, mark):
        self.__number = number
        self.__name = name
        self.__mark = mark

    def get_mark(self):
        return int(self.__mark)

    def get_name(self):
        return self.__name

    def get_number(self):
        return int(self.__number)
