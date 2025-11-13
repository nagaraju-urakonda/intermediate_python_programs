#program to print the sum of digits of a number.
n = int(input("enter a number "))
s = 0
while n:
    s += n % 10
    n = n // 10
    
print(s)
    
