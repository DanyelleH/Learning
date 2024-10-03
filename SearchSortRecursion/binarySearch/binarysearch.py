def binarySearch(arr,value):
    # middle = len(arr) // 2
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = (start + end) //2 # the middle index of the list
        if arr[middle] == value:
            return middle
        if arr[middle] > value:
            end = middle-1
        if arr[middle] < value:
            start =middle+1
    return -1
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 10)) # 2
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 95)) # 16
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 100)) # -1