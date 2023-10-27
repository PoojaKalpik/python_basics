#find largest or smallest element in list
my_list = [10,5,8,3,7,2,4,6,1,9]
#consider 1st element to be largest(or smallest) and compare with other elements
largest = my_list[0]
#compare with all elements of list except 1st element
for i in my_list[1:]:
    #for smallest if i < smallest:
    if i > largest:
        largest = i
print("The largest element in the list is : ", largest)