#Urdu to English and Englis to urdu Dictionary
myDict = {"urdu":"english",
"english":"urdu"
}
print("options are", myDict.keys())                     #returns list of present dict keys
a = input("enter your word\n")
print("the meaning of your word is:", myDict.get(a))    #this dictionary method instead of 'print(myDict[a])' will help to avoid errors even if the words entered those are not present in dictionary. error in progamming is never considered a good sign as it causes to create many problems.
