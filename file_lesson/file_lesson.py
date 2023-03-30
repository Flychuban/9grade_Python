import os

def writeFile():
    my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \n sed do eiusmod tempor incididunt ut labore et dolormagna aliqua. Ut enim ad minim veniam, \n quis nosrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequatDuis aute irure  \n dolor in reprehenderit in voluptate velit esse cillum doloreu fugiat nulla pariatur. Excepteur  \n sint occaecat cupidatat non proident, sunin culpa qui officia deserunt  \n mollit anim id est laborum."
    
    with open("./file_lesson/test.txt", "w") as file:
        file.write(my_text)


def rewrite_file(file_name, number_lines):
    text_in_file =''
    with open("./file_lesson/test.txt", "r") as file:
        for i in range(number_lines):
            text_in_file = text_in_file + file.readline()
    with open(f"./file_lesson/{file_name}.txt", "w") as file:
        file.write(text_in_file)

def reversed_order_write():
    text_in_file = ''
    with open("./file_lesson/test.txt", "r") as file:
        text_in_file = file.readlines()
    text_in_file = reversed(text_in_file)
    
    with open("./file_lesson/reversed_text_file.txt", "w") as file:
        for line in text_in_file:
            file.write(line)

def add_elements_file(file_name, my_list):
    with open(f"./file_lesson/{file_name}.txt", "a") as file:
        for el in my_list:
            file.write("\n" + el)
            

def add_elements_infront_file(file_name, my_list):
    with open(f"./file_lesson/{file_name}.txt", "a") as file:
        pass
    with open(f"./file_lesson/{file_name}.txt", "r+") as file:
        previous_content = file.read()
        file.seek(0, 0)
        for i, el in enumerate(my_list):
            file.write(el.rstrip('\r\n') + '\n')
        file.write(f"\n{previous_content}")

def rename_file():
    os.rename("./file_lesson/infront_list_file.txt",
              "./file_lesson/renamed_infront_list_file.txt")
                
if __name__ == "__main__":
    writeFile()
    add_elements_infront_file("infront_list_file", ["baba", "kote", "mote", "kuche"])
    # rename_file()
    