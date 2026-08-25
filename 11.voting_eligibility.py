age=int(input("Enter Your Age:"))
nat=input("Are you Indian(y,n):")
nat=nat.lower()
if age>=18 and nat=="y":
    print("You are Eligible to vote!")
else:
    print("Sorry, You are not Eligible to vote!")
