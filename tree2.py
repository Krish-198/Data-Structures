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
def Insert(root,k):
    if root==None:
        return Tree(k)
    if root.data>k:
        root.leftnode=Insert(root.leftnode,k)
    else:
        root.rightnode=Insert(root.rightnode,k)
    return  root
def Search(root,key):
    if root.data==key:
        return root
    elif root.data>key and root.leftnode is not None:
        return Search(root.leftnode,key)
    elif root.data>key and root.rightnode is not None:
        return Search(root.rightnode,key)
    else:
        return -1
    
j=int(input("Enter The Number Of elements need in the tree: "))
root=None
for i in range(j):
    x=int(input("Enter the node value: "))
    root=Insert(root,x)
InorderTraversal(root)
key=int(input("Enter the number to be searched: "))
v=Search(root,key)
if v==-1:
    print("Key does not exsist")
else:
    print("Key exsists: ",v.data,'Found')
