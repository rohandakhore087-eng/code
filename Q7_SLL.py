class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Student added successfully!")

    def delete_student(self, roll):
        temp = self.head
        prev = None
        while temp and temp.roll != roll:
            prev = temp
            temp = temp.next
        if not temp:
            print("Student not found!")
            return
        if prev:
            prev.next = temp.next
        else:
            self.head = temp.next
        print("Student deleted successfully!")

    def update_student(self, roll):
        temp = self.head
        while temp and temp.roll != roll:
            temp = temp.next
        if not temp:
            print("Student not found!")
            return
        temp.name = input("Enter new name: ")
        temp.marks = float(input("Enter new marks: "))
        print("Record updated successfully!")

    def search_student(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print(f"Found -> Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
                return
            temp = temp.next
        print("Student not found!")

    def sort_records(self, key='roll', order='asc'):
        if not self.head:
            print("No records to sort!")
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if key == 'roll':
                    a, b = temp.roll, temp.next.roll
                else:
                    a, b = temp.marks, temp.next.marks
                if (order == 'asc' and a > b) or (order == 'desc' and a < b):
                    # Swap data
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next
        print("Records sorted successfully!")

    def display_records(self):
        if not self.head:
            print("No records to display!")
            return
        temp = self.head
        print("\n--- Student Records ---")
        while temp:
            print(f"Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next

# --- Menu-driven program ---
students = StudentList()

while True:
    print("\n--- STUDENT RECORD MENU ---")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Records")
    print("6. Display Records")
    print("7. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        r = int(input("Enter Roll No: "))
        n = input("Enter Name: ")
        m = float(input("Enter Marks: "))
        students.add_student(r, n, m)
    elif ch == 2:
        r = int(input("Enter Roll No to delete: "))
        students.delete_student(r)
    elif ch == 3:
        r = int(input("Enter Roll No to update: "))
        students.update_student(r)
    elif ch == 4:
        r = int(input("Enter Roll No to search: "))
        students.search_student(r)
    elif ch == 5:
        print("Sort by: 1.Roll No  2.Marks")
        k = int(input("Enter choice: "))
        key = 'roll' if k == 1 else 'marks'
        order = input("Order (asc/desc): ")
        students.sort_records(key, order)
    elif ch == 6:
        students.display_records()
    elif ch == 7:
        print("Exiting program... Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
