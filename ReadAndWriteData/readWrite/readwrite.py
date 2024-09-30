# mary_lyrics = ["Mary had a little lamb",
# "Its fleece was white as snow;",
# "And everywhere that Mary went",
# "The lamb was sure to go."]

# with open('/Users/danyelleridley/Documents/Learning/ReadAndWriteData/readWrite/Mary.txt','w') as outfile:
#     for line in mary_lyrics:
#         outfile.write(line + '\n')

# with open('/Users/danyelleridley/Documents/Learning/ReadAndWriteData/readWrite/Mary.txt','r') as infile:
#     for line in infile:
#         print(line.strip())
import json

people = ['William', 'Patrick', 'Jon', 'Tom', 'Peter', 'Colin', 'Sylvester', 'Paul', 'Chris', 'David', 'Matt', 'Peter', 'Jodie']
dictionary = {}
key= 1 # start the dictionary at a key of 1
with open("/Users/danyelleridley/Documents/Learning/ReadAndWriteData/readWrite/numbers.json",'w') as outfile:
    for value in people:
        dictionary[key] = value
        key +=1 # add 1 to the value of Key every loop.
    json.dump(dictionary,outfile)


with open("/Users/danyelleridley/Documents/Learning/ReadAndWriteData/readWrite/numbers.json","r") as infile:
    dictionary = json.load(infile)
    print(dictionary)