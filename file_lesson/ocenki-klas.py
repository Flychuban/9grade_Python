import datetime

def ocenki_klas(file_name):
    file_text = ""
    all_6 = []
    num_4 = 0
    average_mark = 0
    with open(f"./file_lesson/{file_name}", "r", encoding='utf-8') as file:
        file_text = file.readlines()
        for line in file_text:
            line = line.rstrip()
            if "6" in line[-1]:
                all_6.append(line[2:-2])
            elif "4" in line[-1]:
                num_4 += 1
            
            average_mark += int(line[-1])
        
        average_mark = average_mark / len(file_text)
    
    with open("./file_lesson/ocenki-klas-result.txt", "w", encoding='utf-8') as file:
        file.write("Учениците които имат оценка 6 са: ")
        for person in all_6:
            file.write(person + "\n")
        file.write(f"Учениците които имат оценка 4 са {num_4} на брой \n")
        file.write(f"Средно аритметичната оценка е: {average_mark} \n")
        
        if average_mark < 4.5:
            file.write("Контролното беше трудно! \n")
        else:
            file.write("Контролното беше лесно! \n")
            
        date = datetime.datetime.now()
        file.write(f"{date.hour}h:{date.minute}min - {date.day}/{date.month}/{date.year}")
                


if __name__ == "__main__":
    result = ocenki_klas("9a.txt")