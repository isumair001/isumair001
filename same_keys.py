'''IF the names are same of two friends, what will happen to the programe '''
favelang = {}
a = input("Enter your name Ali\n")
b = input("Enter your name Ahmed\n")
c = input("Enter your name Ali\n")
d = input("Enter your name Amal\n")

favelang['Ali'] = a
favelang['Ahmed'] = b
favelang['Ali'] = c
favelang['Amal'] = d

print(favelang)

#keys should not be the same in dictionary, otherwise the later key's value will be shown in results.
