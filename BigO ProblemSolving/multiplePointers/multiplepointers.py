def sumZero(arr):
    # pointer method: declare a left and right pointer.
    left = 0 
    right =len(arr)-1
    while left < right:
        current_sum = arr[left] + arr[right]# array at index 0, + array value at the end of the array.

        if current_sum == 0:
            return [arr[left], arr[right]] #return the value in the array corresponding to the index where L and R are currently at.
        if current_sum < 0:
            left +=1 # if the sum is less than 0 ( negative), we need to moce the left ( lower ) pointer up, increasing the lopwest number to bring it closer to zero.
        else:
            right -=1 #if ythe sum is greater than 0 ( positive) , we need to decrease the highest number, bringing the sum closer to zero.
    return -1 # if no -2 values result in a sum of Zero, the function returns -1


   
print(sumZero([-3, -2, -1, 0, 1, 2, 3]))
print(sumZero([-10, -5, 0, 1, 3, 5, 87, 99])) # [-5, 5]
print(sumZero([-2, 0, 1, 3])) # -1
print(sumZero([1, 2, 3])) # -1