import random
minRand = 10000
maxRand = minRand*10
numbers = list(range(minRand, maxRand))
numbers2 = list(range(minRand, maxRand))
random.shuffle(numbers)
random.shuffle(numbers2)
totNum1,totNum2 = 0,0
totAccCreated = 0

class Account:
    def __init__(self, fName, lName, pin, accNum,balance):
        self.fName = fName
        self.lName = lName
        self.pin = pin
        self.accNum = accNum
        self.balance = balance

accountDict = {}
accountDatabase = []

def getAccNumber():
    accNum,num = False,3
    while num and accNum==False:
        accNum = int(input("Enter Account Number: "))
        if accNum not in accountDict:
            print("Account does not exist")
            num-=1
            accNum = False
    return accNum

def getPin(index):
    pin,num = False,3
    while num and pin==False:
        pin=input("Enter Account Pin: ")
        if pin != accountDatabase[index].pin:
            print("Pin is not correct")
            num-=1
            pin = False
    return pin

def printAccDetails(account):
    print("")
    print("These are your account details: ")
    print(f"Account number: {account.accNum}")
    print(f"First Name: {account.fName}")
    print(f"Last Name: {account.lName}")
    print(f"Account Balance: #{account.balance}")
    print("")
    
def getAccount(withPin=True):
    accNumber = getAccNumber()
    if accNumber==False:
        print("You have failed too many times")
        return False
    index = accountDict[accNumber]
    account = accountDatabase[index]
    if withPin==False:
        return account
    accPin = getPin(index)
    if accPin == False:
        print("You have failed too many times")
        return False
    return account

def getNewAccount(fName,lName,pin,balance=0.00):
    global totAccCreated,totNum1,totNum2
    rand = numbers[totNum1]*100000+numbers2[totNum2]
    totNum2+=1
    if totNum2==len(numbers2):
        totNum2=0
        totNum1+=1
    totAccCreated+=1
    accountDict[rand]=len(accountDict)
    accountDatabase.append(Account(fName,lName,pin,rand,balance))
    return accountDatabase[-1]

printAccDetails(getNewAccount("Chima","Chinedu","1122",120000))
printAccDetails(getNewAccount("Joy","Okoh","3344",500000))
printAccDetails(getNewAccount("Samuel","Chidi","5566",1000000))
printAccDetails(getNewAccount("Chita","Chiamaka","7788",11000000))