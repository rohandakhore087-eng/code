queue=[]
n=int(input("Enter the Size of Queue: "))

def add():
    global queue, n
    if len(queue)==n:
        print("Queue id Full! ")
    else:
        event=input("Enter the event to be inserted: ")
        queue.append(event)
        print("Event Added Successfully.")
    

def longest_event():
    global queue, n
    if(queue):
        val=queue.pop(0)
        print("Process the Longest Event: ",val)
    else:
        print("queue is Empty.")

def pending_event():
    global queue, n
    if(queue):
        print("Display the Pending Event: ",queue)
    else:
        print("There is No Event to Display.")

def cancel_event():
    global queue, n
    if(queue):
        key=input("Enter the Event to be Cancelled: ")
        if key in queue:
            queue.remove(key)
            print("Event is Cancelled.")
        else:
            print("Event Not Found in Queue.")
    else:
        print("Queue is Empty.")


while(True):
    print("--- Event Queue System ---")
    print("1. Add new Event to the Queue")
    print("2. Process the Longest Event")
    print("3. Display the Pending Event")
    print("4. Cancel the Event")
    print("5. Exit")
    
    choice=int(input("Enter choice: "))
    
    if(choice==1):
        add()
    
    elif(choice==2):
        longest_event()
    
    elif(choice==3):
        pending_event()
        
    elif(choice==4):
        cancel_event()
    
    elif(choice==5):
        print("Thank You! for using Real Time Event Processing System")
        break
    
    else:
        print("Invalid Choice")
