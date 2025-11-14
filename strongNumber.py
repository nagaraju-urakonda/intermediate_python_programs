#perfect number
n = int(input("enter a number"))
dummy = n
s = 0

while n:
    digit = n % 10
    fact = 1
    for i in range(1,digit+1):
        fact *= i
    s += fact
        
    n = n // 10
if dummy == s:
    print("strong number")
else:
    print("not a string number")
    