def recur(a):
    if(a>0):
        b=recur(a-1)
        print("out",b)
    return a
a=5
recur(a)
