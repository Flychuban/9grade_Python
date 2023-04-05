from contact import Contact

class PhoneDiary:
    def __init__(self) -> None:
        self._phone_diary = []
        
    def add_contact(self, contact: Contact):
        self._phone_diary.append(contact)
    
    def update_contact(self, searched_name, new_phone_number):
        for person in self._phone_diary:
            if person._name == searched_name:
                person._phone_number = new_phone_number
                break

    def delete_contact(self, searched_name):
        self._phone_diary = [person for person in self._phone_diary if person._name != searched_name] 
    
    def __str__(self) -> str:
        diary_str = ""
        for person in self._phone_diary:
            diary_str += f"{person._name} : {person._phone_number} : {person._sec_number} : {person._email} : {person._instagram_profile} : {person._facebook_profile}" + '\n'
        return diary_str
    
    def write_to_file(self, file_name):
        with open(file_name, 'w+') as file:
            file.write(self.__str__())
        print("Successfully written to file!")
        
    def read_from_file(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            for line in lines:
                name, phone_number, sec_number, email, instagram_profile, facebook_profile = line.split(':')
                contact = Contact(name, phone_number, sec_number, email, instagram_profile, facebook_profile)
                self._phone_diary.append(contact)
        print("Successfully read from file!")
                
        
