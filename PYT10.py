#Class Rectangle
class rectangle:
    def __init__(self,length,breadth):
        self.l=length;
        self.b=breadth;

    def area(self):
        return self.l * self.b 
x=float(input("Enter Length:"));
y=float(input("Enter breadth:"));
r=rectangle(x,y);
print("Area of Rectangle=%s cm^2"%(r.area()))
