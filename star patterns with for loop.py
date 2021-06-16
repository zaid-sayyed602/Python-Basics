n=int(input("Enter the number of lines you want\n:"))
print("1")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
    
print("\n")
print("\n")
print("2")
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
    
print("\n")
print("\n")
print("3")
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()


print("\n")
print("\n")
print("4")
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i-1):
        print("*",end="")
    print()


print("\n")
print("\n")
print("5")
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

print("\n")
print("\n")
print("6")
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-2*i-1):
        print("*",end="")
    print()

print("\n")
print("\n")
print("7")
for i in range(n-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-2*i-1):
        print("*",end="")
    print()


print("\n")
print("\n")

print("8")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end="")
    print()


print("\n")
print("\n")
print("9")
for i in range(n-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i):
        print("*",end="")
    print()    


print("\n")
print("\n")
print("10")
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(n):
        print("*",end="")
    print()

print("\n")
print("\n")
print("11")
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n):
        print("*",end="")
    print()


print("\n")
print("\n")
print("12")
for i in range(n-1):
    for j in range(n-i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()


print("\n")
print("\n")
print("13")
for i in range(n-1):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()

print("\n")
print("\n")
print("14")
for i in range(n-1):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i):
        print("* ",end="")
    print()
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()

print("\n")
print("\n")
print("15")
for i in range(n):
    for j in range(i+1):
        if(i==0 or j==0 or i==n-1 or j==i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
print("\n")
print("\n")
print("16")
for i in range(n):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        if(i==0 or j==0 or i==n-1 or j==i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
print("\n")
print("\n")
print("17")
for i in range(n-1):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-2*i-1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
