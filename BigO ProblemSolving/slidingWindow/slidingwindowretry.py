def maxSubListSum(num_list, num):
    if len(num_list) < num :
        return None
    greatest_sum = 0
    current_sum = 0
    for i in range(num): # for 4 numbers, 
        greatest_sum += num_list[i] # add the value at the index of i to the greaterst sum total.
    current_sum = greatest_sum
    for j in range(num, len(num_list)):# in this case, j would start at num, and proceed to the end of the list.
        current_sum = current_sum - num_list[j-num] + num_list[j]
        #the current sum is the current_sum minus the value in num_list that is at index(j-num(4 in this example))
        # for the first itertion, j=4, and j- 4 = 0( first position); plus  num_list at index 4 (position 5)
        # add the calue one index higher, and subtract the index corresponding j-num
        greatest_sum = max(greatest_sum, current_sum)
    return greatest_sum


print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 2)) # 10
print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 4)) # 17
print(maxSubListSum([4, 2, 1, 6], 1)) # 6
print(maxSubListSum([4, 2, 1, 6, 2], 4)) # 13
print(maxSubListSum([], 4)) # None