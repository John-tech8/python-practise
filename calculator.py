def add (a,b):
    return a+b
def subract (a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide(a,b):
    return a/b

print("Basic Calculator")
print("1.Add")
print("2.Subract")
print("3.Multiply")
print("4.Divide")
choice=int(input("Enter your choice:"))
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))


if choice==1:
    print(f"Result:{add(num1,num2)}")
elif choice==2:
    print(f"Result:{subract(num1,num2)}")
elif choice==3:
    print(f"Result:{multiply(num1,num2)}")
elif choice==4:
    print(f"Result:{divide(num1,num2)}")

else:
    print("Invalid choice")
