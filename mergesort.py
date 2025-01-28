#Divide and Conquer Algorithm
#Time Complexity - O(nlogn)
def merge(a,low,mid,high):
    l=[]
    start1=low
    start2=mid+1
    while start1<=mid and start2<=high:
        if a[start1]<a[start2]:
            l.append(a[start1])
            start1=start1+1
        else:
            l.append(a[start2])
            start2+=1
    while start1<=mid:
        l.append(a[start1])
        start1=start1+1
    while start2<=high:
        l.append(a[start2])
        start2=start2+1
    p=0
    for i in range(low,high+1):
        a[i]=l[p]
        p+=1
def mergesort(x,low,high):
    if low<high:
        mid=(low+high)//2
        mergesort(x,low,mid) #First Partition
        mergesort(x,mid+1,high) #Second Partition
        merge(x,low,mid,high)
    
a=[12,54,78,43,9,72,0,45,23]
j=len(a)
mergesort(a,0,j-1)
print(a)