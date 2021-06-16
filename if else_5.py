no1=int(input(("enter the no1 : ")))
no2=int(input(("enter the no2 : ")))
print("1.ADD\n  2.SUBB\n    3.MUL\n     4.DIV\n")
choice=int(input("enter your choice"))
if(choice==1):
    c=no1+no2
    print(c)

if(choice==2):
    c=no1-no2
    print(c)
    
if(choice==3):
    c=no1*no2
    print(c)
    
if(choice==4):
    c=no1/no2
    print(c)
