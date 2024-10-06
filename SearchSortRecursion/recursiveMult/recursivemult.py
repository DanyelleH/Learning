def multiply(num1, num2, addition_list=None):
    if addition_list == None:
        addition_list=[]
    if num2 == 1:
        addition_list.append(num1)
        return sum(addition_list)
    
    addition_list.append(num1)
    return multiply(num1,(num2-1), addition_list) # carry the additions list through each recursion


print(multiply(7,4))