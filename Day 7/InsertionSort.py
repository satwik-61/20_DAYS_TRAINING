# Insertion Sort
l=list(map(int,input().split()))
n=len(l)
for i in range(1,n):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key

print(l)

# Best Case is O(N) , precisely it's O(N-1)
# Worst case is O(N^2) 