def list_max(num_list,maximum=None):
    if len(num_list) == 0:
        return maximum
    
    if maximum == None:
        maximum = num_list[0]

    if num_list[0] > maximum:
        maximum = num_list[0]
    return list_max(num_list[1:], maximum)
    
print(list_max([1,2,3,56,4,5]))

