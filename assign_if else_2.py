sub1=int(input("Enter the marks of the first subject\n:-"))
sub2=int(input("Enter the marks of the second subject\n:-"))
sub3=int(input("Enter the marks of the third subject\n:-"))
if(sub1>sub2 and sub1>sub3):
    print("Hightest marks is in first subject",sub1)
elif(sub2>sub1 and sub2>sub3):
    print("Hightest marks is in second subject",sub2)
else:
    print("Hightest marks is in third subject",sub3)
    
