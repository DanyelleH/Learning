class OutOfRangeError(Exception):
    pass
def name_the_number(num):
    try:
        if num == 1 or num == 2 or num == 3:
            return(num)
        else:
            raise OutOfRangeError
    except OutOfRangeError:
        return("Number out of range")
    
print(name_the_number(int(input("Pick a number. "))))

    