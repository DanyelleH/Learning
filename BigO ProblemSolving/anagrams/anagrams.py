def validAnagram(string1, string2):
    if len(string1) != len(string2):
        return False
    string1c = string1.split(" ")
    string2c = string2.split(" ")
    for character in string1:
        if character in string2:
            string1c.remove(character)
            string2c.remove(character)
        else:
            return False
    # if len(string1c) == len(string2c):
    #     return True
    
print(validAnagram('aaz', 'zza')) # false
print(validAnagram('anagram', 'nagaram')) # true
print(validAnagram('rat', 'car')) # false
print(validAnagram('qwerty', 'qeywrt')) # true
