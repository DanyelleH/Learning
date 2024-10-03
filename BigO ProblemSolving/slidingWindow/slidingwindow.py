def maxSubListSum(arr, num):
    #num is the LENGTH of the subarray., the index it wants to start at.
    if len(arr) < num:# num represents the index to stop?
        return None
    max_sum =sum(arr[:num])
    current_sum = max_sum
    for i in range(num,len(arr)): # i is where " Num" starts
        current_sum = current_sum - arr[i-num] + arr[i]
        if current_sum> max_sum:
            max_sum = current_sum
    return max_sum

    

print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 2)) # 10
print(maxSubListSum([1, 2, 5, 2, 8, 1, 5], 4)) # 17
print(maxSubListSum([4, 2, 1, 6], 1)) # 6
print(maxSubListSum([4, 2, 1, 6, 2], 4)) # 13
print(maxSubListSum([], 4)) # None