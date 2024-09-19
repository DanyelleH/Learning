# # #Code along file.

# # string_1 = 'Hello'
# # string_2 = " whats good"

# # print( string_1 + string_2)
# # print(f'This is the first string {string_1} and this is the second string {string_2}')


# nums =[1,2,3,4,5]
# for num in nums:
#     num = num*2

# # ** List comprehension loop.**

# double_nums =[2 * num for num in nums]
# # for numbers in nums list, multiple nums by 2



# #only evens
# only_evens = [num for num in nums if num%2 ==0]
# # looking at every number in the list, if that number is divisible by 2, evenly, add to only_evens list.


# # Dictionaries

# state_capitals ={
#     "washington" : " Olympia",
#     "Oregon": "Salem",
#     "Idaho" : "Boise",
#     "Montana": "Helena"
# }

# state_capitals["Texas"] = "Austin"


# del state_capitals["Montana"]


# # Iteration over dictionaries.
# for state in state_capitals.keys():
#     print(state)
# print(state_capitals.keys())
# print(state_capitals.values())
# for capitals in state_capitals.values():
#     print (capitals)

# for key,value in state_capitals.items():
#     print(key,value)
# print(state_capitals.items())


# loopint through  with Index.
word= "dictionary"
for letter, index in enumerate(word):
    print(letter, index)
