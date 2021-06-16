num1=int(input("enter the first no\n"))
num2=int(input("enter the second no\n"))
print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.DIV")
choice=int(input("enter your choice\n"))
if(choice==1):
    c=num1+num2
    print(c)
elif(choice==2):
    c=num1-num2
    print(c)
elif(choice==3):
    c=num1*num2
    print(c)
elif(choice==4):
    c=num1/num2
    print(c)
else:
    print("invalid input")
    
