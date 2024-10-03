def sumZero(arr):
    # pointer method: declare a left and right pointer.
    left, right = 0, len(arr)-1
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == 0:
            return [arr[left], arr[right]]
        if current_sum < 0:
            left +=1
        else:
            right -=1
    return -1


   
print(sumZero([-3, -2, -1, 0, 1, 2, 3]))
print(sumZero([-10, -5, 0, 1, 3, 5, 87, 99])) # [-5, 5]
print(sumZero([-2, 0, 1, 3])) # -1
print(sumZero([1, 2, 3])) # -1