#Median of Three Numbers
a=float(input("Enter First Number: "));
b=float(input("Enter Second Number: "));
c=float(input("Enter Third Number: "));
if a>b :
    if a<c:
        median=a;
    elif b>c:
        median=b;
    else: median=c;
else:
    if a>c:
        median=a;
    elif b<c:
        median=b;
    else: median=c;

print("The Median is :",median);
