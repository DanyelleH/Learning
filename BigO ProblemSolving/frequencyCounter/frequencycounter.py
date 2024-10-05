def same(list_1,list_2):
    if len(list_1) != len(list_2):
        return False

    list_1_frequency ={}
    list_2_frequency ={}
    for value in list_1:
        if value in list_1_frequency:
            list_1_frequency[value] += 1 # if that values in the dictionary, increase the count
        else:
            list_1_frequency[value] = 1

    for value in list_2:
        if value in list_2_frequency:
            list_2_frequency[value] += 1
        else: 
            list_2_frequency[value] = 1
    for key in list_1_frequency.keys():
        if key**2 not in list_2_frequency:
            return False
        if list_1_frequency[key] != list_2_frequency[key**2]:
            return False
    return True



# for value in list_1.copy():
#     value2=value**2
#     if (value2) in list_2.copy():
#         list_1.remove(value)
#         list_2.remove(value2)
#     else:
#         break
# if len(list_1)==0 and len(list_2) == 0:
#     return True
# return False

            

print(same([1, 2, 3], [4, 1, 9])) # true
print(same([1, 2, 1], [4, 4, 1]))
print(same([1, 2, 1], [4, 4, 1])) # false (must be same frequency)