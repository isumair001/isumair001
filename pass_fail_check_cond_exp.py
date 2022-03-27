#ALT + click for multi cursors in vscode editor

#To find whether a student is pass or fail if it requires a total of 50% and atleast 33% in each subject to pass.

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))


"using conditional exprressions"
if (sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% marks in any of your subjects")

elif(sub1+sub2+sub3)/3 <50:
    print("you are failed because you have aggregate marks less than 40%")
else:
    print("Congratulations! You have successfully passed your examination as a whole")
