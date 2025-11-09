def selection(salary):
    n=len(salary)
    for i in range(0, n-1):
        min=i
        for j in range(i+1, n):
            if(salary[j]<salary[min]):
                min=j
        salary[i], salary[min]=salary[min], salary[i]
    print(salary)
    #salary.reverse()
    print("Top 5 Highest Salaries: ", salary[-5:][::-1])


def bubble(salary):
    swapped=False
    n=len(salary)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if(salary[j]>salary[j+1]):
                salary[j], salary[j+1]= salary[j+1], salary[j]
                swapped=True

        if not swapped:
            break
        
    print(salary)
    #salary.reverse()
    print("Top 5 Highest Salaries: ", salary[-5:][::-1])

    
salary = []
a=int(input("Enter the number of Employee: "))
for i in range(a):
    arr=float(input("Enter the Employee Salary: $ "))
    salary.append(arr)
    
print(salary)

c=input("Enter the sorting method (selection/bubble): ")

if(c=='selection'):
    selection(salary)

elif(c=='bubble'):
    bubble(salary)

else:
    print("Invalid Choice")   
    
