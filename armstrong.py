def armstrong(n):
    temp=n
    sum=0
    k=len(str(n))
    

    while n>0:
        digit=n%10
        sum=sum+digit**k
        n=n//10


    if sum == temp :
        print("Armstrong")

    else:
        print("Not a Armstrong")
num=int(input("Enter a Number:"))
armstrong(num)
