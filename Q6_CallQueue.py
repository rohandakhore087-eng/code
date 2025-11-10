callcenter=[]

def addCall():
    global callcenter, customerID, callTime
    customerID=int(input("Enter the Customer ID: "))
    callTime=int(input("Enter call Time in Minute: "))
    call={"customerID":customerID, "callTime":callTime}
    callcenter.append(call)
    print(f"customerID {customerID} is added with its callTIme {callTime}min")
    

def answerCall():
    if(callcenter):
        answer=callcenter.pop(0)
        print(answer)

    else:
        print("No Calls to Answer.")

def viewQueue():
    if(callcenter):
        print(callcenter)

    else:
        print("No Calls in the Queue.")

def isQueueEmpty():
    if(callcenter):
        print("Queue is not Empty.")

    else:
        print("Queue is Empty.")
    

while(True):
    print("---Call System---")
    print("Select the Operation to Perform.")
    print("1. Add call with its CustomerID and callTime.")
    print("2. Remove first call.")
    print("3. Display the calls.")
    print("4. Check if the Queue is Empty.")
    print("5. Exit")

    choice=int(input("Enter the choice:"))

    if(choice==1):
        addCall()

    elif(choice==2):
        answerCall()

    elif(choice==3):
        viewQueue()

    elif(choice==4):
        isQueueEmpty()

    elif(choice==5):
        print("Thank You")
        break

    else:
        print("Invalid Choice")
