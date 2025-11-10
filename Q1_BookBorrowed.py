def average(borrow):
    add = 0
    for i in range(0, len(borrow)):
        add = add+borrow[i]
        avg = add/n
    print("Average Number of Borrowed Book are: ",avg)

def highestlowest(borrow):
    if not borrow:
        print("There are no Book Present")
    else:
        highest=borrow[0]
        lowest=borrow[0]

        for i in range(len(borrow)):
            if (borrow[i]>borrow[0]):
                highest=borrow[i]
            if(borrow[i]<borrow[0]):
                lowest=borrow[i]

        print("Highest Number of Book Borrowing is: ",highest)
        print("Lowest Number of Book Borrowing is: ",lowest)
        
        
    

def zerocount(borrow):
    zero_count=borrow.count(0)
    print(f"Zero count book is: {zero_count}")

def mode(borrow):
    mode=0
    max_freq=1
    for i in range(n):
        freq=borrow.count(borrow[i])
        if(freq>max_freq):
            max_freq=freq
            mode=borrow[i]
    print("Most Frequent Borrow Count (mode):",mode)


n=int(input("Number of Book: "))

borrow=[]

for i in range(n):
    count=int(input(f"Book Borrow count for Book {i+1}: "))
    borrow.append(count)

print(borrow)

while(True):
    print("--- Menu Driven ---")
    print("1.Calculate the Average of book.")
    print("2.Find Highest and Lowest Borrowed Book.")
    print("3.Calculate Zero Count Book.")
    print("4.Display Most frequent Borrowed Count(Mode).")
    print("5.Exit.")


    choice=int(input("Enter your Choice: "))

    if choice==1:
        average(borrow)

    elif choice==2:
        highestlowest(borrow)

    elif choice==3:
        zerocount(borrow)

    elif choice==4:
        mode(borrow)

    elif choice==5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")


    
