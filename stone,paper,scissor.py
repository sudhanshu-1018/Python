import random
def check(comp,user):
    if comp==user:
        return 0
    elif comp==0 and user==2:
        return -1
    elif comp==1 and user==2:
        return -1
    elif comp==2 and user==1:
        return -1
    return 1



comp=random.randint(0,2)
user=input("choose optioan from given below:\n0=stone\n1=paper\n2=scissor\n(0/1/2):")

score=check(comp,user)
print("user",user)
print("computer",comp)
if score==0:
    print("tie")
elif score==-1:
    print("you loose")
else:
    print("you won")
