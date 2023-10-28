#find an element in the list
my_list = [10,5,8,3,7,2,4,6,1,9]
#element to be found
find_element = 7
#dummy variable to check if the element if found or not
found = 0

for i in my_list:
    if find_element == i:
        print("element:", find_element, "found in list : ", my_list)
        found = 1

#if found is still 0, element is not present in list
if found == 0:
    print("element not found")