# with open('/Users/danyelleridley/Documents/Learning/ReadAndWriteData/classPractice/dog.txt','r') as infile:
#     for line in infile:
#         # print(line) #excess space
#         print(line.strip()) # formatting document, removes white space



# try:
#     with open('/Users/danyelleridley/Documents/Learning/ReadAndWriteData/classPractice/dog2.txt','r') as infile:
#         for line in infile:
#             print(line.strip())
# except FileNotFoundError:
#     print ('The file was not found')
import json

cat_list = ["Siamese", "Manx", 'Abyssinian', "Savannah","Ragdoll"]
with open('/Users/danyelleridley/Documents/Learning/ReadAndWriteData/classPractice/cats.txt', 'w') as outfile:
    for cat in cat_list:
        outfile.write(cat + "\n")



import json

cat_list = ["Siamese", "Manx", 'Abyssinian', "Savannah","Ragdoll"]
with open('/Users/danyelleridley/Documents/Learning/ReadAndWriteData/classPractice/cats.json', 'w') as outfile:
    json.dump(cat_list,outfile)#dump that into there.

with open('/Users/danyelleridley/Documents/Learning/ReadAndWriteData/classPractice/cats.json', 'r') as infile:
    restored_list = json.load(infile)
    print(restored_list)
# with open('/Users/danyelleridley/Documents/Learning/ReadAndWriteData/classPractice/numbers.txt','w') as outfile:
#     for number in range(1,11):
#         outfile.write(str(number) + '\n')