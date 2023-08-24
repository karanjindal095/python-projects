def atm():
    bal = 60000
    acc_no = 12346789
    pin = 1610
    user = int(input("Enter the acc no : "))
    if(user == acc_no):
        E_pin = int(input("Enter the pin : "))
        if(E_pin == pin):
                ask = input("you want to deposit or withdraw the amount (d/w) : ")
                if(ask == "d"):
                    deposit = float(input("enter the amount you want to deposit : "))
                    balance = bal + deposit 
                    print("Your Account no : ",acc_no)
                    print("Your current balance is : ",balance)
                    print("Thank You")
                elif(ask == "w"):
                    withdraw = float(input("Enter the Amount you want to withdraw : "))
                    if(withdraw > bal ):
                        print("Sorry!! Insufficient Balance ")
                    else:
                        balance = bal - withdraw
                        print(balance)
                        print("Your Account no : ",acc_no)
                        print("Your current balance is : ",balance)
                        print("Thank You")
        else:
            print("Wrong pin!! try again")
            atm()
    else:
        print("Wrong account number !! try again")
        atm()
    
    
atm()
