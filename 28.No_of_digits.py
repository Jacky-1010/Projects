num=int(input("Enter no.:"))
i=0
x=num
while num!=0:
    num=num//10
    i+=1
print(f"The no. of digits in {x} is {i}")
