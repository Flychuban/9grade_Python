# 1. ex
from re import A
from unicodedata import digit


def sumDigits(number):
    sum = 0
    while number:
        sum += number % 10
        number //= 10
    return sum
    
# 2. ex
def intToList(number):
    arr = []
    while number:
        arr.append(number % 10)
        number //= 10
    arr.reverse()
    return arr 

# 3. ex
def listToInt(arr):
    numberInt = 0
    for digit in arr:
        numberInt = numberInt * 10 + digit
    return numberInt


# 4. ex
def fibonachiNum(n):
    a = 0
    b = 1
    fibonachi_number = 0
    res = b
    for i in range(n):
        multiply = 10 ** len(str(res))
        fibonachi_number = fibonachi_number * multiply + res
        if i%2 == 0:
            a = a + b
            res = a
        else:
            b = a + b
            res = b
    # for i in range(2, n):
    #     print(list(a))
    #     yield a
    #     b = a + b 
        
    return fibonachi_number


#5. ex
def isBalanced(number):
    numList = intToList(number)
    is_len_odd = False
    numDigits = len(numList)
    
    if numDigits % 2 == 1:
        is_len_odd = True
        
    middle = numDigits // 2
    arr1 = numList[:middle]
    
    if is_len_odd:
        arr2 = numList[middle + 1:]
    else:
        arr2 = numList[middle:] 
        
    sum1 = 0
    sum2 = 0 
    for digit in arr1:
        sum1 += digit
    for digit in arr2:
        sum2 += digit
    
    if(sum1 - sum2 == 0):
        return True
    else:
        return False
 

# 6. ex
def isDecreasingSequence(arr):
    for i in range(1 ,len(arr)):
        if arr[i] >= arr[i - 1]:
            return False
    return True

    
if __name__ == "__main__":
    a = fibonachiNum(5)
    print(a)