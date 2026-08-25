ch=input("Enter a character:")
vow=["a","e","i","o","u"]
if char in vow:
    print(ch," is a vowel")
elif char not in vow:
    print(ch," is a consonant")
else:
    print("Invalid Input")
