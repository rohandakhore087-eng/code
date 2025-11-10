document=""

undostack=[]
redostack=[]

def change():
    global document, undostack, redostack
    change=input("Enter the text: ")
    undostack.append(document)
    document=document+change
    redostack.clear()
    print("Change has been Done.")

def undo():
    global document, undostack, redostack
    if(undostack):
        redostack.append(document)
        document=undostack.pop()
        print("Undo Operation is done.")
    else:
        print("Nothing to print")

def redo():
    global document, undostack, redostack
    if(redostack):
        undostack.append(document)
        document=redostack.pop()
        print("Redo Operation is done")
    else:
        print("Nothing to Redo.")

def document_state():
    global document
    print("Document State: ",document)



while (True):
    print("---Text Editor---")
    print("Which Operation do you want perform.")
    print("1. Make the change in Document")
    print("2. Undo")
    print("3. Redo")
    print("4. Document State")
    print("5. Exit")

    choice=int(input("Enter the choice: "))

    if(choice==1):
        change()

    elif(choice==2):
        undo()

    elif(choice==3):
        redo()

    elif(choice==4):
        document_state()

    elif(choice==5):
        print("Thank You for Using Undo-Redo System.")
        break

    else:
        Print("Invalid Choice")
