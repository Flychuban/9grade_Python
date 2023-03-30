from phone_diary import PhoneDiary
from contact import Contact

if __name__ == "__main__":
    misho = Contact("Misho Polendakov", "0101010101")
    nikola = Contact("Nikola Petrov", "0707070707")
    vito = Contact("Vitorio Shotev", "0606060606")
    
    # maria = Contact("Maria Pehlivanova", "0999999999")
    # pesho = Contact("Pesho Ivanov", "0666666666")
    # katya = Contact("Katya Ivanova", "0505050505")
    
    phone_diary = PhoneDiary()
    
    
    
    # print(phone_diary)
    # with open("phone_diary.txt", 'w') as file:
    #     file.write("Sth")
    
    # phone_diary.write_to_file(r"C:\Users\sas\Desktop\Vuvedenie_skriptovi_ezici\oop_lesson3\phone_diary.txt")
    
    phone_diary.read_from_file(r"C:\Users\sas\Desktop\Vuvedenie_skriptovi_ezici\oop_lesson3\phone_diary.txt")
    
    phone_diary.add_contact(misho)
    phone_diary.add_contact(nikola)
    phone_diary.add_contact(vito)
    
    phone_diary.update_contact("Maria Pehlivanova", "07777777")

    phone_diary.delete_contact("Pesho Ivanov")
    
    
    phone_diary.write_to_file(r"C:\Users\sas\Desktop\Vuvedenie_skriptovi_ezici\oop_lesson3\phone_diary.txt")
    
        
    
    