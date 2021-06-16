ans=0
q1=input("Are you at Home\n:")
if(q1=="no"):
    ans=ans+25
elif(q1=="yes"):
    ans=ans+0
else:
    print("bad answer")
q2=input("Do you Have any travel history abroad\n:")
if(q2=="yes"):
    ans=ans+25
elif(q2=="no"):
    ans=ans+0
else:
    print("bad answer")

q3=input("Do you have cold, cough, fever or any of the symptoms\n:")
if(q3=="yes"):
    ans=ans+25
elif(q3=="no"):
    ans=ans+0
else:
    print("bad answer")

q4=input("Do you follow the home quarantine\n:")
if(q4=="no"):
    ans=ans+25
elif(q4=="yes"):
    ans=ans+0
else:
    print("bad answer")

print("your possibility of getting covid-19 is",ans,"%")
