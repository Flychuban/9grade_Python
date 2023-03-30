def reverse_reading(search_string, file_write_name):
    text_result = []
    with open("./test_1_17/test.txt", "r") as file:
        first_text = file.readlines()
        for line in first_text:
            line = line.rstrip()
            if search_string in line:
                text_result.append(line[::-1])
                text_result.append("\n")

                
    with open(f"./test_1_17/{file_write_name}", "w") as file:
        print(text_result)
        for line in text_result:
            file.write(line)
            file.write("\n")


def make_dictionary():
    all_stusents_txt= []
    new_dict = {}
    with open("./test_1_17/9a.txt", "r", encoding='utf-8') as file:
        all_stusents_txt = file.readlines()
        for student in all_stusents_txt:
            student = student.rstrip()
            number = student[:2]
            name = student[2:-2]
            new_dict[number] = name
    
    with open("./test_1_17/9a_dict.txt", "w", encoding='utf-8') as file:
        for key,value in new_dict.items():
            new_string = f"{key} : {value}\n"
            file.write(new_string) 
        
        
        

if __name__ == "__main__":
    reverse_reading("bazi", "result_reversed.txt")
    reverse_reading("joker", "result_reversed2.txt")
    reverse_reading("pizza", "result_reversed3.txt")
    make_dictionary()