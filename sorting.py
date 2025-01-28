#Sorting-Rearranging the elements in a specifc order
l=[10,12,9,1,5,0]
l.sort(reverse=False)
print(l)
l.sort(reverse=True)
print(l)
#BubbleSort
#Time Complexity - O(n^2)
p=[90,20,89,28,218,12,89]
for i in range(0,len(p)):
    for j in range(i,len(p)):
        if p[i]<p[j]:
            p[i],p[j]=p[j],p[i]
print(p)
#InserionSort
#Time Complexity - O(n^2)
k=[12,45,67,9304,90,15]

for i in range(0,len(k)):
    d=10000
    g=0
    for j in range(i,len(k)):
        if d>k[j]:
            d=k[j]
            g=j
            k[i],k[j]=k[j],k[i]
print(k)