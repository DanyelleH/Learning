#pseudoCode
def bubbleSort(arr):
#   1. Loop through the list once from start to finsih. --> "x"
    for x in range(len(arr)):
#   2. loop a second (inner) loop and compare "x" to "y"
        for y in range(0,len(arr)-x -1): # from the beginning of the list, to the value of x.
#   3. cmpare x and y; if x is > y
            if arr[y] > arr[y+1]:
                arr[y],arr[y+1] = arr[y+1], arr[y]
    return arr
# if x is greater, switch the variables.
                



# def bubbleSort(uo_list):
#     for x in range(len(uo_list)-1,0,-1):# how many times to loop through the list, starting from the back of the list.
#         for j in range (0,x):
#             if uo_list[j] > uo_list[j+1]:
#                 #swapping
#                 place_holder = uo_list[j]
#                 uo_list[j] = uo_list[j +1]
#                 uo_list[j+1] = place_holder
#     return uo_list

print(bubbleSort([5, 3, 10, 6, 1])) # [1, 3, 5, 6, 10]
print(bubbleSort([100, 98, 101, 10])) # [10, 98, 100, 101]
print(bubbleSort([2, 1, 0, 5, 4])) # [0, 1, 2, 4, 5]