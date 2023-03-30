# 1. from random import Random, randint
# from re import A

# a = []
# for j in range(randint(0, 65432)):
#     a.append(randint(-65432, 65432))

# sum = 0
# for i in a:
#     sum += i
# print(sum)


# 2. from random import randint
# a = []
# for j in range(randint(0, 65432)):
#     a.append(randint(-65432, 65432))

# br = 0
# for i in a:
#     if i%2 == 0:
#         br+=1
# print(br)

# 3. from random import randint

# a = []
# for j in range(randint(0, 432)):
#     a.append(randint(-65432, 65432))

# min = None
# max = None
# for element in a:
#     if a.index(element) == 0:
#         max = element
#         min = element
#     if element < min:
#         min = element
#     elif element > max:
#         max = element
# difference = max - min
# print(difference) 

a = [[3,4,5], [7,14,3]]
sum = 0
for i in a:
    max = None 
    for j in i:
        if i.index(j) == 0:
            max = j
        if j > max:
            max = j 
    sum += max
         
print(sum)