shop=[["oil",50],["rice",40],["wheat",60],["oats",100],["corn",50],["maggi",70],["maida",120],["coke",80],["flour",30],["ice",30]]
cart=[]
choice=0
def addcart(*x):
    flag=0
    for i in range(len(shop)):
        if(shop[i][0]==x[0]):
            temp=[x[0],x[1]]
            cart.append(temp)
            print("Added successfully")
            flag=1
    if(flag==0):
        print("Not in the cart")
    return cart
def remcart(remove1):
    for i in range(len(cart)):
        if(cart[i][0]==remove1):
            cart.remove(cart[i])
            print("Removed successfully")
    return cart        
def bill():
    cnt=0
    flag=0
    for i in range(len(cart)):
        for j in range(len(shop)):
            if(cart[i][0]==shop[j][0]):
                cnt+=cart[i][1]*shop[j][1]
                print(cart[i][0],"=",cart[i][1]*shop[j][1],"/-")
                flag=1
        if(flag==0):
            print("not in the cart")
    return cnt
def exiting():
    print("Exited")
while(choice!=4):
    print("1.ADD ITEMS TO THE CART")
    print("2.REMOVE FORM THE CART")
    print("3.BILL")
    print("4.EXIT")
    choice=int(input("Enteryour choice\n"))
    if(choice==1):
        n=int(input("Enter the no of items you want in the cart\n"))
        for i in range(n):
            itemname=input("Enter the item\n")
            itemquan=int(input("Enter the quantity\n"))
            c=addcart(itemname,itemquan)        
            print(c)

    elif(choice==2):
        itemrem=input("Enter the item you want to remove\n")
        c=remcart(itemrem)
        print(c)
    elif(choice==3):
        total=bill()
        print("Your total bill is",total)
    elif(choice==4):
        exiting()
    else:
        print("Invalid input")
