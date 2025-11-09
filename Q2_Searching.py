def linear(num, key):
    for i in range(len(num)):
        if num[i]==key:
            print("Customer ID Found.")
            return i
    print("Customer ID not found.")        
    return -1        
#Time Complexity= best case O(1) & worst case O(n)            
            
def binary(num, key):
    low=0
    n=len(num)-1
    high=n

    while(low<=high):
        mid=(low+high)//2
        if(num[mid]==key):
            print("Customer ID found.")
            return mid
            
        elif(num[mid]<key):
            low=mid+1
            
        else:
            high=mid-1
    
    print("Customer Id not found.")
    return -1
#Time Complexity= best case O(1) & worst case O(log n)    

num = []
a = int(input("Enter the Number of Customer ID: "))
for i in range(a):
    m=int(input("Enter the customer ID: "))
    num.append(m)
num.sort()    
print(num)

key=int(input("Enter the ID to search: "))

c=input("Select the searching method (linear/binary): ")

if c=='linear':
    linear(num, key)

elif c=='binary':
    binary(num, key)
    
else:
    print("Invalid Choice")

    
    













