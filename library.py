import datetime as d
dep = {"BCA" : ["C++","Python","Java","C"],
       "BBA" : ["Economics","stats","business","English"],
       "Btech" : ["Maths","Ai","ML","Data analysis","Data Science"],
       "Bcom" : ["Accounts","Management","Audit","Marketing"],
       "BA" :["Pshycology","History","Geography","Law"]
}
user = input("Enter the Department : ")
a = 0
print(f"Department {user} has these Books ")
match user:
    case "BCA":
        for i in dep["BCA"]:
            a+=1
            print(a,i)
    case "BBA":
        for i in dep["BBA"]:
            a+=1
            print(a,i)
    case "Btech":
        for i in dep["Btech"]:
            a+=1
            print(a,i)  
    case "Bcom":
        for i in dep["Bcom"]:
            a+=1
            print(a,i)
    case "BA":
        for i in dep["BA"]:
            a+=1
            print(a,i)
    case _:
        print("Department not Matched")
        
book = input("Enter the Book which you want to issue : ")
print("Ok Issuing your book plz enter your details")
A = input("Enter your Name : ")
today = d.date.today()
new_date = today + d.timedelta(days=14)
print(f"Today date is {today}")
print(f"You have to return the Book on {new_date}")
print("Thank you")