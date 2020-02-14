#Triangle
#Equilateral,Isoceles,Scalene
print("Enter the lenght of three sides of a triangle.");
x=int(input("x: "));
y=int(input("y: "));
z=int(input("z: "));
if x==y==z :
    print("The Given Value Forms a Equilateral triangle.");
elif x==y or y==z or z==x :
    print("The Given Value Forms a Isoceles triangle.");
else: print("The Given Value Forms a Scalene triangle.");
