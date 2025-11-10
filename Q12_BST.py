class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # Node with one or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# Menu-driven program
if __name__ == "__main__":
    bst = BST()
    root = None

    while True:
        print("\n--- BINARY SEARCH TREE MENU ---")
        print("1. Insert Node")
        print("2. Delete Node")
        print("3. Search Node")
        print("4. Display Inorder")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to insert: "))
            root = bst.insert(root, val)
            print("Node inserted successfully!")
        elif choice == 2:
            val = int(input("Enter value to delete: "))
            root = bst.delete(root, val)
            print("Node deleted (if existed).")
        elif choice == 3:
            val = int(input("Enter value to search: "))
            found = bst.search(root, val)
            print("Node found!" if found else "Node not found!")
        elif choice == 4:
            print("Inorder traversal of BST: ", end="")
            bst.inorder(root)
            print()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")
