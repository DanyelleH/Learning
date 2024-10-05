'''
larger values "bubbling" to the top; switching with adjacent values until a 
specifc order is reached.
Pseudocode:
    1. Iterate from back of the list towards the front
    2. start an inner loop (nested loop) with variable "j" from beginning to i-1
    3. if list[j] is greater than [j+1], swap the values.
    4. Return a sorted list
'''
def bubbleSort(unordered_list):
    length = len(unordered_list)
    for i in range(length): #1, tracks overall rotations
        for j in range(0,length-i-1): #length - x - 1 prevents rerunning the last index, because after the first iteration we know the last index is the greaest. 
            if unordered_list[j] > unordered_list[j+1]:
                unordered_list[j], unordered_list[j+1] = unordered_list[j+1], unordered_list[j]
    return unordered_list
    
print(bubbleSort([5, 3, 10, 6, 1])) # [1, 3, 5, 6, 10]
print(bubbleSort([100, 98, 101, 10])) # [10, 98, 100, 101]
print(bubbleSort([2, 1, 0, 5, 4])) # [0, 1, 2, 4, 5]
