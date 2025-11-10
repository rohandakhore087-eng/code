# ---------------- HASH TABLE FUNCTIONS ----------------

def create_table(size):
    return [None] * size

def hash_function(key, size):
    return key % size

def insert(table, key, size):
    index = hash_function(key, size)
    start = index
    while table[index] is not None and table[index] != -1:
        if table[index] == key:
            print("Key already exists!")
            return
        index = (index + 1) % size
        if index == start:
            print("Hash Table is Full! Cannot insert.")
            return
    table[index] = key
    print(f"Key {key} inserted at index {index}")

def search(table, key, size):
    index = hash_function(key, size)
    start = index
    while table[index] is not None:
        if table[index] == key:
            print(f"Key {key} found at index {index}")
            return
        index = (index + 1) % size
        if index == start:
            break
    print("Key not found!")

def delete(table, key, size):
    index = hash_function(key, size)
    start = index
    while table[index] is not None:
        if table[index] == key:
            table[index] = -1
            print(f"Key {key} deleted from index {index}")
            return
        index = (index + 1) % size
        if index == start:
            break
    print("Key not found!")

def display(table, size):
    print("\n--- HASH TABLE ---")
    for i in range(size):
        print(f"Index {i}: {table[i]}")
    print("------------------")

# ---------------- MENU DRIVEN PROGRAM ----------------

size = 10
table = create_table(size)

while True:
    print("\n--- HASH TABLE MENU ---")
    print("1. Insert Key")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Table")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        insert(table, key, size)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(table, key, size)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(table, key, size)

    elif choice == 4:
        display(table, size)

    elif choice == 5:
        print("Thank You for Using Hash Table System.")
        break

    else:
        print("Invalid Choice!")
