def lang(r1=0,r2=0,a1=0,a2=0,a4 = 0):
    a = input("Enter the text : ")
    k = 0
    if(k != a.isspace()):
        print("no space allowed")
        return 0
    elif(a.isascii()):
        print("eligile answer")
    b = int(input("Enter 1 for encoding , 0 for decoding : "))
    d = 0
    if(b==1):
        d = True
    elif(b==0):
        d = False
    else:
        print("quit")
    if(d == True):
        r1 = "ogh"
        r2 = "lic"
        a1 = r1[:] + a[1:] + a[0] + r2[:]
        print(a1)
    elif(d == False):
       a2 = a[3:-4] 
       a4 =  a[-4] + a2[:]
       print(a4)

lang()
lang()