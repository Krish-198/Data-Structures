class Tree:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None
def InorderTraversal(root):
    if root.leftnode != None:
        InorderTraversal(root.leftnode)
    print(root.data)
    if root.rightnode != None:
        InorderTraversal(root.rightnode)

def PreorderTraversal(root):
    print(root.data)
    if root.leftnode != None:
        PreorderTraversal(root.leftnode)
    if root.rightnode != None:
        PreorderTraversal(root.rightnode)


def PostorderTraversal(root):
    if root.leftnode != None:
        PostorderTraversal(root.leftnode)
    if root.rightnode != None:
        PostorderTraversal(root.rightnode)
    print(root.data)
def create_tree():

    root = Tree(int(input("Enter the root: ")))
    root.leftnode = Tree(int(input("Enter the left node: ")))
    root.rightnode = Tree(int(input("Enter the right node: ")))
    root.leftnode.leftnode = Tree(int(input("Enter the left child of left node: ")))
    root.leftnode.rightnode = Tree(int(input("Enter the right vhild of left node: ")))
    root.rightnode.leftnode = Tree(int(input("Enter the left child of right node: ")))
    return root

def menu():
    print("\nMenu:")
    print("1. Create Tree")
    print("2. Inorder Traversal")
    print("3. Preorder Traversal")
    print("4. Postorder Traversal")
    print("5. Exit")
    
    try:
        choice = int(input("\nEnter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return None

def main():
    tree = None
    while True:
        choice = menu()
        if choice is None:
            continue
            
        if choice == 1:
            tree = create_tree()
            print("Tree created successfully!")
        elif choice == 2:
            if tree:
                print("\nInorder Traversal:")
                InorderTraversal(tree)
            else:
                print("No tree created yet. Please create a tree first.")
        elif choice == 3:
            if tree:
                print("\nPreorder Traversal:")
                PreorderTraversal(tree)
            else:
                print("No tree created yet. Please create a tree first.")
        elif choice == 4:
            if tree:
                print("\nPostorder Traversal:")
                PostorderTraversal(tree)
            else:
                print("No tree created yet. Please create a tree first.")
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()

