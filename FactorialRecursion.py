def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
b=int(input("Enter the number"))
print("The factorial of",b,"is",factorial(b))