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

root=Tree(4)
root.leftnode=Tree(3)
root.rightnode=Tree(2)
root.leftnode.leftnode=Tree(9)
root.leftnode.rightnode=Tree(8)
root.rightnode.leftnode=Tree(7)
InorderTraversal(root)
PreorderTraversal(root)
PostorderTraversal(root)