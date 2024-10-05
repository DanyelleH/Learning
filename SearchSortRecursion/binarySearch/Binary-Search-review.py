''' Binary search is a divde and conquor method, Requires list to be sorted.
if the value youre looking at is too small, increase the left pointer, if it is too large, decrease the r pointer. 

'''
def binarySearch(sorted_list, target_value):
    #return index where the value exists
    #the L and R pointers indicate the index
    left = 0
    right = len(sorted_list) -1
    while left <=right:
        middle_point = (left + right) //2
        if sorted_list[middle_point] == target_value:
            return middle_point
        if sorted_list[middle_point] > target_value:
            right = middle_point -1
        if sorted_list[middle_point] < target_value:
            left = middle_point +1
    return -1 
    
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 10)) # 2
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 95)) # 16
print(binarySearch([5, 6, 10, 13, 14, 18, 30, 34, 35, 37, 40, 44, 64, 79, 84, 86, 95, 96, 98, 99], 100)) # -1