numbers=list(map(int,input("Enter Numbers Seperated By Space:").split()))
max_value=numbers[0]
for i in numbers:
    if i > max_value:
        max_value=i
print(f"The Maximim value is {max_value}")
        
