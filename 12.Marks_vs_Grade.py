mks=int(input("Enter Marks:"))
if mks>=90 and mks<=100:
    print("Grade A")
elif mks>=75 and mks<=89:
    print("Grade B")
elif mks>=60 and mks<=74:
    print("Grade C")
elif mks>=40 and mks<=59:
    print("Grade D")
elif mks<40:
    print("Grade F")
else:
    print("Invalid Input")
