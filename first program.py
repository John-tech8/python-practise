def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
result=gcd(num1,num2)
print(f"The Gcd of {num1} , {num2} is {result}")
