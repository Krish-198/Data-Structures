l1=["{","(","["]
l2=["}",")","]"]
def braketmatching(x):
    stack=[]
    for i in x:
        if i in l1:
            stack.append(i)
        elif i in l2:
            j=l2.index(i)
            if((len(stack)>0) and (l1[j]==stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced!"
    if len(stack)==0:
        return "Balanced!"
    else:
        return "Unbalanced!"
b="{blah}(hhk"
print("string- ",braketmatching(b))