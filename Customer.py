import database
        
def printAccount():
    print("Welcome to View Account Details!")
    account = database.getAccount()
    if account==False:
        return False
    database.printAccDetails(account)
    return True

def createNewAccount() :
    print("Welcome to Create a New Account!")
    fName=input("Enter Customer First Name: ")
    lName=input("Enter Customer Last Name: ")
    pin=input("Enter your pin: ")
    account = database.getNewAccount(fName,lName,pin)
    database.printAccDetails(account)
    return True

def transferFund():
    print("Welcome to Transfer Funds!")
    print("Input account details to transfer from")
    account1 = database.getAccount()
    if account1==False:
        return
    print("Input account details to transfer to")
    account2 = database.getAccount(False)
    if account2==False:
        return
    amount = float(input("Enter the amount to be transfered: "))
    if amount <= 0:
        print("Invalid amount!")
        return False
    if account1.balance < amount:
        print("Insufficient funds!")
        return False
    account1.balance-=amount
    account2.balance+=amount
    database.printAccDetails(account1)
    print(f"#{amount} has been transferred successfully to {account2.fName} {account2.lName}")
    return True

def resetPassword():
    print("Welcome to Change Pin!")
    print("Input your account details")
    account = database.getAccount()
    newPin = input("Enter your new pin: ")
    newPin2 = input("Confirm your new pin: ")
    if newPin!=newPin2:
        print("Pins do not match!")
        return False
    account.pin = newPin
    database.printAccDetails(account)
    return

def exitProgram():
    print("Thanks for visiting, see you next time!")
    return

def printStart():
    print("Welcome toChita's Bank Management System for Customers!")
    print("0 = Exit the Program")
    print("1 = Create a new Account")
    print("2 = View Account Info")
    print("3 = Transfer to an Account")
    print("4 = Reset Password")
    key = input("Type a key to choose your option: ")
    return int(key)

key = 1
while key!=0:
    key = printStart()
    print("")
    if key==0:
        exitProgram()
    elif key==1:
        createNewAccount()
    elif key==2:
        printAccount()
    elif key==3:
        transferFund()
    elif key==4:
        resetPassword()
    else:
        print("That is an invalid option")
    print("")  