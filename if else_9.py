no1=int(input("enter the value for no1 :"))
no2=int(input("enter the value for no2 :"))
print("1.ADD2.SUB3.MUL4.DIV")
choice=int(input("enter your choice"))
if(choice==1):
    c=no1+no2
    print("addition is ",c)

if(choice==2):
    c=no1-no2
    print("substraction is ",c)

if(choice==3):
    c=no1*no2
    print("multipication is ",c)

if(choice==4):
    c=no1/no2
    print("division is ",c)
                
