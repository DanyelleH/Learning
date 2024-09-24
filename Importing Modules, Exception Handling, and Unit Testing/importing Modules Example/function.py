def sum(num_1,num_2):
    sum = num_1 + num_2
    return sum
def subtraction(num_1,num_2):
    difference = num_1 - num_2
    return difference

def main():# input code not meant to be run by other modules.
    result = sum(2,4)
    print(result)


if __name__ == "__main__":
    main() # if thu8nder name is equal to main, the run the main funtion. if the file is an import, dont run code from the original file.


# print (__name__,"i am functions.py") # returns in terms of wehats being ran. ran here, returns main, because its being used in "main" file.
#when imported to a different file, it returns where the