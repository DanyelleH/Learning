# def countUniqueValues(arr):
    # if not arr:
    #     return " Object is not an List"
    # return (len(set(arr)))
#set removes duplicates.
#length retruens the length of the new array, without duplicates

## ** This solution is better because it has a lower space complexity due to it being constant, instead of using the Set operation.
def countUniqueValues(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return 1
    
    left = 0
    right =1
    unique_values =1
    while right != len(arr):
        if arr[left] != arr[right]: # if index 0 of the array does not equal index 1, add to unique_values value.
            unique_values +=1
            left = right
        elif arr[left] == arr[right]:
            right += 1
    return unique_values

print(countUniqueValues([1, 1, 1, 1, 1, 2])) # 2
print(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])) # 7
print(countUniqueValues([-2, -1, -1, 0, 1])) # 4
print(countUniqueValues([])) # 0

# space_complexity = O(1)
# time_complexity = O(n)