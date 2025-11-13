#counting digits in number
n = int(input("enter a number"))

count = 0

while n:
    count += 1
    n = n // 10
print(count)