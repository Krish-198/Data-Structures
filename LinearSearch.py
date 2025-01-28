print("Linear Search: ")
l=list(map(int,input("Enter the number:").split()))
k=int(input("Enter the key: "))
if k in l:
    print("Key exsists")
else:
    print("Key does not exist")

#Time complexity of the linear algorithm is 0(n)
print("***************************************************************************************************************")
print("Binary Seacrh")
def binary_search(l1,low,high,k):
    mid=(low+high)//2
    if low<=high:
        if l1[mid]==k:
            return mid
        elif l1[mid]<k:
            return binary_search(l1,mid+1,high,k)
        elif l1[mid]>k:
            return binary_search(l1,low,mid-1,k)
    else:
        return -1
            
print(binary_search([0,1,2,3,4,5,6,7,8],0,8,3))