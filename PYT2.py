#Filename_Extension
f=input("Enter The File Name With Extension:");
index=0;
for i in range(len(f)):
    if f[i]=='.':
        index=i
print(f[index+1: ])
    
