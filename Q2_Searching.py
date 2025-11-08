def linear(num,key):
    for i in range(len(num)):
        if num[i]==key:
            return i
    return -1

def binary(num,key):
    start=0
    end=len(num)-1
    while(start<=end):
        mid=(start+end)//2

        if num[mid]==key:
            print("Customer ID is found")
            return mid

        elif num[mid]<key:
            start=mid+1

        else:
            end=mid-1

        return -1    

    
    print("Customer id not found")
    return -1

num=[]
a=int(input("Enter number of id"))
for i in range(a):
    n=int(input("Enter customer id"))
    num.append(n)
print(num)     

key=int(input("Enter id to search"))

c=input("Which method do you want linear or binary")

if c=='linear':
    x=linear(num,key)
    if x!=-1:
        print("Customer id found")
    else:
        print("customer id not found")

elif c=='binary':
    binary(num,key)
else:
    print("Error")
