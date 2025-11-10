class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print("Key updated successfully!")
                return
        self.table[index].append([key, value])
        print("Key inserted successfully!")

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Key found! Value = {pair[1]}")
                return
        print("Key not found!")

    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print("Key deleted successfully!")
                return
        print("Key not found!")

    def display(self):
        print("\n--- Hash Table ---")
        for i in range(self.size):
            print(f"[{i}] -> {self.table[i]}")

# Menu-driven part
if __name__ == "__main__":
    ht = HashTable()

    while True:
        print("\n--- HASH TABLE MENU ---")
        print("1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key: "))
            value = input("Enter value: ")
            ht.insert(key, value)
        elif choice == 2:
            key = int(input("Enter key to search: "))
            ht.search(key)
        elif choice == 3:
            key = int(input("Enter key to delete: "))
            ht.delete(key)
        elif choice == 4:
            ht.display()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")
