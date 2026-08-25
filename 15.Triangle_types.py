side1=float(input("Enter the length of fist Side(in meters):"))
side2=float(input("Enter the length of second Side(in meters):"))
side3=float(input("Enter the length of third Side(in meters):"))
if side1==side2==side3:
    print("Triangle is Equilateral")
elif side1==side2 or side2==side3 or side1==side3:
    print("Triangle is Isosceles")

else:
    print("Triangle is Scalene")
