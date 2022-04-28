
#string
#s.upper()
#s.lower()

name = "Nadeem Sumair"
print(name.upper())
print(name.lower())

print("*********************")

#find position

print(name.find("Sumair"))

print("*********************")

#s.replace("old name", "new name"))

print(name.replace("Nadeem Sumair","Ali Saeed"))
print(name)

print("*********************")
#to check if string or part of string is in main string?

print("Sumair" in name)
print("a" in name)
print("s" in name)

print("*********************")
#to check s.startswith() and s.endswith()

print(name.startswith("Nad"))
print(name.endswith("air"))


print("*********************")

#remove white space using split() and seprate the sub strings

name = "            Nadeem Sumair   "
c = name.strip(" ")
print(c)
c = name.split()
print(c)

print("****************")

