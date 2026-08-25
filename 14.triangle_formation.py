side1=float(input("Enter the length of side 1(in meters):"))
side2=float(input("Enter the length of side 2(in meters):"))
side3=float(input("Enter the length of side 3(in meters):"))

if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print(side1, side2, side3," form a triangle")
else:
    print(side1, side2, side3," do not form a triangle")
