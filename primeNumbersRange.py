n = int(input("enter number"))
if n < 2:
    print("not prime")
for n in range(2,n+1):
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            break
    else:
        print(n, end = " ")
