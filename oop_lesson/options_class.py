from student_class import Student

class Options:
    def __init__(self, file_text, average_mark, all_students) -> None:
        self.__file_text = file_text
        self.__average_mark = average_mark
        self.__all_students = all_students

    def make_students(self):
        for line in self.__file_text:
            line = line.rstrip()
            number = line[:2]
            name = line[2:-2]
            mark = line[-1]
            student = Student(number, name, mark)
            self.__all_students.append(student)
            self.__average_mark += student.get_mark()

    def get_all_6(self):
        all_6 = []
        for student in self.__all_students:
            if student.get_mark() == 6:
                all_6.append([student.get_number(), student.get_name()])
        return all_6

    def get_num_4(self):
        num_4 = 0
        for student in self.__all_students:
            if student.get_mark() == 4:
                num_4 += 1
        return num_4

    def get_average_mark(self):
        self.__average_mark = self.__average_mark / len(self.__all_students)
        return self.__average_mark
