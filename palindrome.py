num=int(input("Enter a Number:"))
temp=num
reverse=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
if temp ==reverse:
        print("palindrome")
else:
        print ("not a palindrome")
