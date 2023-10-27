#list of integers from 1-10 
my_list = [1,2,3,4,5,6,7,8,9,10]

#using slice we create a new copy of list for all oprations
my_list_1 = my_list[:]
#will be using print function after each operation to know the result
print("new list is : ", my_list_1)

#eleminate 1st and last element using slice
my_list_2 = my_list_1[1:-1]
print("after eleminating 1st and last element : ", my_list_2)

#accessing list elements 
first_element = my_list_1[0]
last_element = my_list_1[-1]
print("the first and last element which were deleted are : ", first_element, last_element)

#length of list
length_of_list = len(my_list_1)
print("the length of list is : ", length_of_list)

#delete extra list, even few elements can be deleted from list
del my_list_2
del my_list_1[2:4]
print("new list after deleting few elements is : ", my_list_1)

# adding list elemets
my_list_3 = my_list[:]
#append adds an element to the end of list
my_list_3.append(15)
#insert adds an element to the desired location in list
my_list_3.insert(2,20)
print("new list after adding elements is : ", my_list_3)

#list comprehensions can be used to reduce lines of code
#lets multiply each elemet in list my_list with 2 and create a new list
my_list_4 = [i*2 for i in my_list]
print("new list which is old list multiplied by 2 is : ", my_list_4)