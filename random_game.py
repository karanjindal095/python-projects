import random as r
print("Choose from below\n","0 for snake\n","1 for water\n","2 for gun\n")
user = int(input("Enter your choice : "))
if(user < 0 or user > 2):
    raise ValueError("value should be b/w 0 & 2")
print("\n")
comp = r.randint(0,2)
def dis(d):
    a,b,c=0,0,0
    if(d == 0):
        a = "snake"
        print("Your choice      : ",d,a)
    elif(d == 1):
        b = "water"
        print("Your choice      : ",d,b)
    elif(d == 2):
        c = "gun"
        print("Your choice      : ",d,c)
dis(user)
def dis(d):
    a,b,c=0,0,0
    if(d == 0):
        a = "snake"
        print("computer's choice : ",d,a)
    elif(d == 1):
        b = "water"
        print("computer's choice : ",d,b)
    elif(d == 2):
        c = "gun"
        print("computer's choice : ",d,c)
dis(comp)
def check(user,comp):
    if(user == comp):
        return 0
    elif(user == 0 and comp == 2):
        return -1
    elif(user == 1 and comp == 0):
        return -1
    elif(user == 2 and comp == 1):
        return -1
    return 1
score = check(user,comp)
if(score == 0):
    print("Its draw")
elif(score == -1):
    print("You loose")
else:
    print("You win")
