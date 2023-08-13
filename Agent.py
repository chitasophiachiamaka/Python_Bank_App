import database
    
def depositFund():
    print("Welcome to Deposit Funds!")
    print("Input the account details you want to deposit to")
    account = database.getAccount(False)
    if account==False:
        return False
    amount = float(input("Enter the amount to be deposited: "))
    if amount <= 0:
        print("Invalid amount!")
        return False
    account.balance+=amount
    database.printAccDetails(account)
    return True

def resetPassword():
    print("Welcome to Reset Password!")
    remember = input("Do you know the old password? Type 'y' for yes or any key for no: ")
    print("Input the account details")
    if remember=="y":
        account = database.getAccount()
    else:
        account = database.getAccount(False)
    if account==False:
        return False
    
    if remember!="y":
        fullName = account.fName+account.lName
        temp = account.fName[0]+'*'*(len(account.fName)-1)
        temp += account.lName[0]+'*'*(len(account.lName)-1)
        temp2 = input(f"Input the full text replacing the * with correct letters: {temp}\n")
        if temp2!=fullName:
            print("Wrong answer")
            return False
    newPin = input("Enter your new pin (Type 'c' to quit): ")
    if newPin=='c':
        return False
    newPin2 = input("Confirm your new pin (Type 'c' to quit): ")
    if newPin2=='c':
        return False
    if newPin!=newPin2:
        print("Pins do not match!")
        return False
    account.pin = newPin
    database.printAccDetails(account)
    return True

def exitProgram():
    print("Thanks for visiting Our Bank, see you next time!")
    return

def printStart():
    print("Welcome to Chita's Bank Management System for Agents!")
    print("0 = Exit the Program")
    print("1 = Deposit to an Account")
    print("2 = Change Customer Account Pin")
    key = input("Type a key to choose your option: ")
    return int(key)

key = 1
while key!=0:
    key = printStart()
    print("")
    if key==0:
        exitProgram()
    elif key==1:
        depositFund()
    elif key==2:
        resetPassword()
    else:
        print("That is an invalid option")
    print("")
        