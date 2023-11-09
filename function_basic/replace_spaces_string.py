#function to remove space from a given string
def remove_space(s):
    return s.replace(" ","")

#get a valid input string from user
sentence = input("enter a sentence to remove spaces from: ")

#get result using the function
space_removed = remove_space(sentence)

#print the output
print(space_removed)