def all_words_count(my_str):
    all_words = my_str.split()
    all_words_set = set(all_words)
    all_words_dict = {}
    for word in all_words_set:
        all_words_dict[word] = all_words.count(word)
    
    sorted_dict = sorted(all_words_dict.items(), reverse=True ,key=lambda x: x[1])
    sorted_keys = [item[0] for item in sorted_dict]
    return sorted_keys

def is_permutation(my_arr):
    for i in range(len(my_arr)):
        my_arr[i].sort()
        
    permutation_indexes = []
    for i in range(len(my_arr) - 1):
        for j in range(i + 1, len(my_arr)):
            if my_arr[i] == my_arr[j]:
                if i in permutation_indexes:
                    permutation_indexes.append(j)
                else:
                    permutation_indexes.extend((i, j))
                break
        
    return permutation_indexes
    
    

if __name__ == "__main__":
    result = all_words_count("baba kote mote asd asd baba baba")
    result2 = all_words_count("baba baba baba baba dqdo baba baba")
    result3 = all_words_count("kotka kuche petel mishka")
    print(result)
    print(result2)
    print(result3)
    
    # result = is_permutation([[1, 2, 3], [4, 5, 6], [3, 2, 1]])
    # result2 = is_permutation([[1, 2, 3], [5, 4, 6] , [4, 5, 6], [3, 2, 1]])
    # result3 = is_permutation([[1, 2, 3], [3, 1, 2], [3, 2, 1], [2, 1, 3], [2, 2, 3]])
    # print(result)
    # print(result2)
    # print(result3)
    
    