from work_files import WorkFile
from student_class import Student
from options_class import Options
            
def ocenki_klas(r_file, w_file):
    average_mark = 0
    all_students = []
    
    work_file = WorkFile(r_file, w_file)
    file_text = work_file.read_from_file()
    
    student_options = Options(file_text, average_mark, all_students)
    student_options.make_students()
    all_6 = student_options.get_all_6()
    num_4 = student_options.get_num_4()
    average_mark = student_options.get_average_mark()
    
    work_file.write_in_file(all_6, num_4, average_mark)


if __name__ == "__main__":
    result = ocenki_klas("./oop_lesson/9a.txt",
                         "./oop_lesson/ocenki-klas-result.txt")
