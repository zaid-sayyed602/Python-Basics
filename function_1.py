    #----BASIC FUCNTION-----
def add():
    a=2
    b=3
    c=a+b
    print(c)
add()
#----PARAMETERIZED FUNCTION----
def add(x,y):
    c=x+y
    print(c)
a=5
b=5
add(a,b)    
#-----RETURN FUNCTIONS-------
def add(x,y):
    z=x+y
    return z
c=add(5,2)
print(c)
#-----MULTIPLE RETURN FUNCTION WITH TUPLE-----
def add(x,y):
    z=x+y
    return x,y,z
c=add(5,2)
print(c)
#-----MULTIPLE RETURN FUNCTION WITH SEPERATE VALUE-----
def add(x,y):
    z=x+y
    return x,y,z
l,m,n=add(5,2)
print(l,m,n)
#-----MULTIPLE PARAMETER FUNCTION------
def add(*x):
    z=x[0]+x[1]
    print(z)
add(20,30)
'''METHOD 2
def add(*x):
    z=x[0]+x[1]
    return z
c=add(20,30)
print(c)'''
#-----DEFAULT FUNCTION------
def add(a,b,c=0):
    z=a+b
    return z
c=add(a=30,b=30)
print(c)
