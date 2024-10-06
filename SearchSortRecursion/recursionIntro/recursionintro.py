'''
Recursion: The act of a function calling itself.
    All recursive functions have two elements:
        1. A base case: Where the recursive function stops. (condition)

        2. A Recursive call: where the function calls itself.

'''


def countdown(num):
    if num == 0:
        return str(num)
    return (f"{str(num)}, {countdown(num -1)}")
# print(countdown(12))

def countup(num, current=1):
   if current == num:
       return str(current)
   return (f"{str(current)}, {countup(num,current+1)}")

print(countup(10))

def sum_countup(num, current =1, sum_list = []):
    # if sum_list == None:
    #     sum_list=[]
    if current == num:
        sum_list.append(num)
        return sum(sum_list)
    sum_list.append(current)
    return sum_countup(num, current +1, sum_list)
    
print(sum_countup(5))