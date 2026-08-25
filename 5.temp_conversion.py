temp=float(input("Enter the temperature"))
act=int(input("Select the action(1=C-F,2=F-C):"))
if act==1:
    print(temp,"C=",9/5*temp+32,"F")
elif act==2:
    print(temp,"F=",(temp-32)*5/9,"C")
else:
    print("Invalid Input")
