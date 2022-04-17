#Reverse table using for loop
num=int(input("Enter the number"))
for i in range (10,0,-1):
  print(f"{num}*{i}={num*i}")
  
 #Reverse table using while loop

num = int(input("Enter you number"))
i = 10
while i>=1:
    print(f"{num}x{i}={num*i}")
    i = i -1
