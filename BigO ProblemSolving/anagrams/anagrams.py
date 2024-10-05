def validAnagram(string1, string2):
    if len(string1) != len(string2):
        return False
    string1_letters = {}
    string2_letters ={}

    for letter in string1:
        if letter not in string1_letters.keys():
            string1_letters[letter] = 1
        else:
            string1_letters[letter]+=1

    for letter in string2:
        if letter not in string2_letters.keys():
            string2_letters[letter] =1
        else:
            string2_letters[letter] +=1
    for k in string2_letters.keys():
        if k not in string1_letters.keys():
            return False
    for k,v in string2_letters.items():
        if string2_letters[k] != string1_letters[k]:
            return False
    return True

    
print(validAnagram('aaz', 'zza')) # false
print(validAnagram('anagram', 'nagaram')) # true
print(validAnagram('rat', 'car')) # false
print(validAnagram('qwerty', 'qeywrt')) # true
