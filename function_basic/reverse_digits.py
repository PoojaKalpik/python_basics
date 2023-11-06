#function to reverse a given number
def reverse_digit(n):
    ans = 0
    while (n>0):
        ans = (ans *10) + (n % 10)
        n = n//10
    return ans

#get input values from user and use function to reverse the number
n = int(input("Please input a number to be reversed: "))
r = reverse_digit(n)
print("The reverse of number",n,"is",r)