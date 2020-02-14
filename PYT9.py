#Even or Odd
a=[];
n=int(input("Enter Number of Elements:"));
for i in range(0,n):
    nos = int(input("Enter a number:"))
    a.append(nos)
print("The Given List Of Numbers:  ",a);
even=0;
odd=0;
for x in a:
    if not x%2:
        even+=1;
    else: odd+=1;
print("Even Numbers: ",even);
print("Odd Numbers: ",odd);
