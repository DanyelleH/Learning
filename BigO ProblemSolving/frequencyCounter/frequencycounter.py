def same(list_1,list_2):
    for value in list_1.copy():
        value2=value**2
        if (value2) in list_2.copy():
            list_1.remove(value)
            list_2.remove(value2)
        else:
            break
    if len(list_1)==0 and len(list_2) == 0:
        return True
    return False
    
            

print(same([1, 2, 3], [4, 1, 9])) # true
print(same([1, 2, 1], [4, 4, 1]))
print(same([1, 2, 1], [4, 4, 1])) # false (must be same frequency)