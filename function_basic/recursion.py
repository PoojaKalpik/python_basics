#print the fibonacci series for a given integer (sum of previous 2 numbers in a series)

#calculate the fibonacci series for a number using recursion
def fibonacci(number):
    #negative numbers
    if number < 0:
        return None
    #fibonacci series for 1 is 1 and 2 is 1,1
    if number < 3:
        return 1
    #if number is 3 or more calculate the sum of previous 2 numbers in series
    return fibonacci(number-1) + fibonacci(number - 2)

#get input from user using "input" and convert the vlaue to integer
number = int(input("please input the number to calculate fibonacci series :"))

#print the fibinacci series
for i in range(1,number+1):
    #end =",", separates the output with a ","
    print(fibonacci(i), end=",")
#this adds and "enter" at the end
print("")