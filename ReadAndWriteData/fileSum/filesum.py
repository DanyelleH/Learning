numbers_list = [23.77, 116, 94, -12.8, 0, 14.999]
with open("/Users/danyelleridley/Documents/Learning/ReadAndWriteData/fileSum/numbers_list.txt","w") as outfile:
    for number in numbers_list:
        outfile.write(str(number) + "\n")

def file_sum(text_file):
    try:
        with open(text_file, 'r') as infile:
            num_list =[float(number.strip()) for number in infile]
    except FileNotFoundError:
         return('File Not Found')
    with open("/Users/danyelleridley/Documents/Learning/ReadAndWriteData/fileSum/sum.txt",'w') as outfile:
            total = sum(num_list)
            outfile.write(str(total))
            

file_sum("/Users/danyelleridley/Documents/Learning/ReadAndWriteData/fileSum/numbers_list.txt")