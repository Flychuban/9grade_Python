from operator import itemgetter

# 1.ex
# def printSimultaneously(list1, list2):
#     used_len = None
#     if len(list1) < len(list2):
#         used_len = len(list1)
#     else:
#         used_len = len(list2)
#     for i in range(used_len):
#         print(f"{list1[i]} - {list2[len(list2) - i - 1]}")

# 2 ex.
# def concatOrdered(list_1, list_2):
#     result = []
#     for big_word in list_1:
#         for small_word in list_2:
#             result.append(big_word + small_word)
#     return result

# 3 ex.
# result = extract_dict({
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New York"
# }, ["name", "salary"])
# print(result)

# def extract_dict(sample_dict, output_keys):
#     extracted_dict = {}
#     for key in output_keys:
#         extracted_dict[key] = sample_dict.get(key)
#     print(extracted_dict)
#     return extract_dict


# 4 ex.
# result = lowest_value({
#     "Physics": 82,
#     "Math": 65,
#     "History": 75
# })
# print(result)

# def lowest_value(my_marks):
#     lowest_value = 0
#     lowest_key = ""
#     for i, (key,value) in enumerate(my_marks.items()):
#         if i == 0:
#             lowest_value = value
#             lowest_key = key
#         elif value < lowest_value:
#             lowest_value = value
#             lowest_key = key
#     return lowest_key


# 5 ex.
# result = unpack_tuple((10, 20, 30, 40))
# print(result)
# print(type(result))
        
# def unpack_tuple(my_tuple):
#     a = my_tuple[0]
#     print(a)
#     b = my_tuple[1]
#     print(b)
#     c = my_tuple[2]
#     print(c)
#     d = my_tuple[3]
#     print(d)
#     return (a, b, c, d)

# 6 ex.
# def sort_tuple(my_tuple):
#     sorted_2item = tuple(sorted(my_tuple, key=lambda tup: tup[1]))
#     # list(my_tuple).sort(key=itemgetter([1]))
#     return sorted_2item

#7 ex.
# def list_to_set(my_set, my_arr):
#     my_set.update(tuple(my_arr))
#     return my_set

def two_sets_union(set1, set2):
    my_union = set1.intersection(set2)
    return my_union
    
    
if __name__ == "__main__":
    result = two_sets_union({"Yellow", "Orange", "Black"}, {"Blue", "Green", "Orange"})
    print(result)