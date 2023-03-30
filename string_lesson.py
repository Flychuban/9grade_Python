from operator import le
import re

# ex 1.
# def is_anagram(str1, str2):
#     my_dict_1 = {}
#     my_dict_2 = {}
#     str1 = str1.lower()
#     str2 = str2.lower()
    
#     if len(str1) != len(str2):
#         return False
#     for letter in range(len(str1)):
#         my_dict_1[str1[letter]] = str1.count(str1[letter])
#         my_dict_2[str2[letter]] = str2.count(str2[letter])
#     if my_dict_1 != my_dict_2:
#         return False
#     return True        


# ex. 2
# def count_words(given_words):
#     my_dict = {}
#     for word in given_words:
#         my_dict[word] = given_words.count(word)
#     return my_dict


# ex. 3
# def nan_expand(n):
#     if n<1:
#         return ""
#     result_str = ("Not a ") * n + "NaN"
#     return result_str


# ex.4 
# def group(my_list):
#     grouped_list = []
#     longest_subsequence = 1
#     current_subsequence = 1
#     small_list = [my_list[0]]
#     for i in range(1, len(my_list)):
#         if my_list[i] == my_list[i - 1]:
#             small_list.append(my_list[i])
#             current_subsequence += 1
#         else:
#             grouped_list.append(small_list)
#             if current_subsequence > longest_subsequence:
#                 longest_subsequence = current_subsequence
#             current_subsequence = 1
#             small_list = [my_list[i]]
#     grouped_list.append(small_list)
#     if current_subsequence > longest_subsequence:
#         longest_subsequence = current_subsequence
#     return [grouped_list, longest_subsequence]


# 5 ex.
# def sum_numbers_str(my_string):
#     new_number = 0;
#     for symbol in my_string:
#         if symbol.isnumeric():
#             new_number = new_number * 10  + int(symbol)
#     return new_number


# 6 ex.
# def find_gas_station(distance, tank_size, stations):
#     possible_options = []
#     if stations[0] > tank_size:
#         return None
#     if stations[1] > tank_size:
#         possible_options.append(stations[0])
#     else:
#         possible_options.append(stations[1])
#     for i in range(2, len(stations) - 1):
#         if stations[i] - stations[i - 1] > tank_size:
#             return None
#         elif stations[i + 1] - possible_options[-1] > tank_size:
#             possible_options.append(stations[i])
#     if distance - stations[-1] > tank_size:
#         return None
#     elif distance - possible_options[-1] > tank_size:
#         possible_options.append(stations[-1])
#     return possible_options
        
        
# additional ex. 1
# def count_words_from_file():
#     my_dict = {}
#     with open("words.txt", "r", encoding='utf-8') as file:
#         words_file = file.readline()
#         all_words = words_file.split()
#         for word in all_words:
#             my_dict[word] = all_words.count(word)
#         print(all_words)
#     return my_dict

def sort_words_from_file():
    my_dict = {}
    words_file_1 = ""
    all_words = ""
    with open("words.txt", "r", encoding='utf-8') as file:
        words_file_1 = file.read()
        all_words = words_file_1.split()
        all_words.sort()
        for word in all_words:
            my_dict[word] = all_words.count(word)
        print(all_words)
    
    sorted_str = ""
    for word in all_words:
        sorted_str = sorted_str + word + " "
    
    
    with open("newfile.txt", "w") as file:
        file.write(str(my_dict))
        file.write("\n")
        file.write("\n")
        file.write("Unsorted string:\n")
        file.write(words_file_1)
        file.write("\n")
        file.write("Sorted string: \n")
        file.write(sorted_str)
        
        
if __name__ == "__main__":
    result = sort_words_from_file()
    print(result)