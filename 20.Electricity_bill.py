#Electricity Bill for a Simple House with Single phase connection, as per MERC policy during 2025.
#Wheeling charge, Fuel Surcharge, Electricity duty,etc. are not included.

unit=int(input("Enter the units consumed:"))

FC=130


if unit>=0 and unit<=100:
    EC=unit*4.28

elif unit>=101 and unit<=300:
    EC=100*4.28+(unit-100)*11.1
    
elif unit>=301 and unit<=500:
    EC=100*4.28+200*11.1+(unit-300)*15.38

elif unit>500:
    EC=100*4.28+200*11.1+200*15.38+(unit-500)*17.68

else:
    print("Invalid Input")

bill=FC+EC
print(f"The Bill for {unit} units is INR {bill}.")



