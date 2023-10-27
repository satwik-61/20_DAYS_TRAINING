'''
import math
n=int(input())
print(math.floor(math.sqrt(n)))

'''
l=list(map(int,input().split()))
i=int(input())
if i in l:
    print(l.index(i))
else:
    print(-1)

