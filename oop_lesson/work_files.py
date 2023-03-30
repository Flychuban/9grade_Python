import datetime
from student_class import Student


class WorkFile:
    def __init__(self, read_file_name, write_file_name) -> None:
        self.__read_file_name = read_file_name
        self.__write_file_name = write_file_name

    def read_from_file(self):
        file_text = ""
        with open(self.__read_file_name, "r", encoding='utf-8') as file:
            file_text = file.readlines()
        return file_text

    def write_in_file(self, all_6, num_4, average_mark):
        with open(self.__write_file_name, "w", encoding='utf-8') as file:
            file.write("Учениците които имат оценка 6 са: \n")
            for person in all_6:
                file.write(str(person[0]) + " " + person[1] + "\n")
            file.write(
                f"Учениците които имат оценка 4 са {num_4} на брой \n")
            file.write(
                f"Средно аритметичната оценка е: {average_mark} \n")

            if average_mark < 4.5:
                file.write("Контролното беше трудно! \n")
            else:
                file.write("Контролното беше лесно! \n")

            date = datetime.datetime.now()
            file.write(
                f"{date.hour}h:{date.minute}min - {date.day}/{date.month}/{date.year}")
