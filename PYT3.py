#Longest word
def longest(w):
   w_len = [];
   for n in w:
       w_len.append((len(n),n));
       w_len.sort();
   return w_len[-1][1]

x,y,z,p=input("Enter 4 Words:").split();
print(longest([x,y,z,p]));
