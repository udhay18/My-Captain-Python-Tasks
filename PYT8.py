#Multiply All The Numbers In A List
def multiply(n):  
    p = 1
    for i in n:
        p *= i  
    return p
a=int(input("Enter the number: "));
b=int(input("Enter the number: "));
c=int(input("Enter the number: "));
d=int(input("Enter the number: "));
e=int(input("Enter the number: "));
print(multiply((a,b,c,d,e)));
