#check if a specific bit in a given number is set or not
#function that gets the input number and bit and returns True or False
def bit_set(number, bit_number):
    if number & (1<<bit_number):
        return True
    else:
        return False

#input number and bit number
number = int(input("please input number to be checked:"))
bit_number = int(input("please input the bit number, we need to check:"))

yes_or_no = bit_set(number, bit_number)

if yes_or_no:
    print("the given bit in given number is SET.")
else:
    print("the given bit in given number is NOT SET.")