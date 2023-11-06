#function to find second largest value in the list
def print2largest(arr, n):
    #sort the list in decending order
	arr.sort(reverse = True)
    #if the largest number is repeated, ignore it and take next largest number
	for i in range(n-1):
	    if arr[i] != arr[i+1]: 
	        return arr[i+1]

# list value and length of list 
a1 = [29,26,88,24,36,25,66,63,88,22]
n = 10

s_nd_largest = print2largest(a1,n)

print(s_nd_largest)
