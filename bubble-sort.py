

def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        arr[i].sort()
        flag = 0
        for j in range(i+1, len(arr)):
            if sum(arr[j]) < sum(arr[i]):
                c = arr[i]
                arr[i] = arr[j]
                arr[j] = c
                flag = 1
        if flag == 0:
            break 
    return arr

def sort_2(arr):
    for big_el in arr:
        big_el.sort()
    arr.sort(key=lambda item: sum(item))
    return arr

if __name__ == "__main__":
    arr = [[4, 2, 6], [7, 1, 9], [1, 2, 4], [1, 2, -1]]
    print(sort_2(arr))