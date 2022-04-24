n =int(input("Enter the number"))
if n>2:
    for i in range(2,n):
        if n % i == 0:
            print("it is not a prime number")
            break
        else:
            print("It is prime number")
            break
elif n==2:
    print("It is a prime number")
else:
    print("It is not a prime number")
