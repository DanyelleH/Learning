def is_decreasing(num_list):
    if len(num_list) <=1:
        return True
    
    if num_list[0] <= num_list[1]:
        return False
    
    return is_decreasing(num_list[1:])
    

print(is_decreasing([105,100,66,47,135,32,20,15]))