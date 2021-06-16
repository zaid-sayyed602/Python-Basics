ans=0
q1=input("Do you know Python?\n:")
if(q1=="yes"):
    ans=ans+12
elif(q1=="no"):
    ans=ans+0
else:
    print("bad answer")
q2=int(input("How good are you at maths(rate your self form scale of 1 to 10)\n:"))
if(q2==10):
    ans=ans+11
elif(q2<10 and q2>=6):
    ans=ans+8
elif(q2<=6 and q2>=2):
    ans=ans+5
elif(q2<=2):
    ans=ans+3
elif(q2==0):
    ans=ans+0
else:
    print("bad answer")
q3=input("How good are you at communication\n:")
if(q3=="excelent"):
    ans=ans+12
elif(q3=="good"):
    ans=ans+9
elif(q3=="average"):
    ans=ans+4
elif(q3=="poor"):
    ans=ans+0
else:
    print("bad answer")
q4=input("Are you a team player\n:")
if(q1=="yes"):
    ans=ans+9
elif(q1=="no"):
    ans=ans+0
q5=input("Do you have any experience\n:")
if(q1=="yes"):
    ans=ans+9
elif(q1=="no"):
    ans=ans+0
ans1=ans/100*100    
print("As per your answers your percentage is",ans1)
if(ans1>35):
    print("!!!!Congrats!!!!\nYou are selected")
else:
    print("!!!!Sorry!!!!\nYou are rejected")
