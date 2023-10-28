#bubble sort to sort a list
my_list = [10,5,8,3,7,2,4,6,1,9]

#dummy variable to check if the list is sorted or not(consider this 1 to get inside the loop)
swapped = 1

# we can just use my_list.sort() to get a sorted list
# and for a list sorted in  decending order we can use my_list.reverse() after sorting the list
while swapped:
    swapped = 0
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            swapped = 1
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print("After sorting the sorted list is : ", my_list)