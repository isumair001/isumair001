#to writea multiplication table program we may use loops. f string is also simplest way to right this program.
num = int(input("Enter the number"))
for i in range(1, 11):
    #print(str(num) + "X" + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}")
