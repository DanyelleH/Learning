def bubbleSortCount(unordered_list):
    length = len(unordered_list)
    comparison_count =0
    exchange_count = 0
    for i in range(length): #1, tracks overall rotations
        for j in range(0,length-i-1): #length - x - 1 prevents rerunning the last index, because after the first iteration we know the last index is the greaest. 
            comparison_count +=1
            if unordered_list[j] > unordered_list[j+1]:
                exchange_count +=1
                unordered_list[j], unordered_list[j+1] = unordered_list[j+1], unordered_list[j]
    return comparison_count, exchange_count

print(bubbleSortCount([1, 2, 3, 5, 4, 6, 7])) # (21, 1)
print(bubbleSortCount([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # (45, 45)
print(bubbleSortCount([2, 1, 0, 5, 4])) # (10, 4)