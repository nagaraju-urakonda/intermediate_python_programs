#checkin if a number is armstrong or not

n = int(input("enter a number "))
power = len(str(n))
dummy = n
s = 0

while n:
    digit = n % 10
    s += digit ** power
    n = n // 10
if s == dummy:
    print("it is a armstrong number")
else:
    print("not a armstrong")