a=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25
n=1
n2=2
x=0
for i in a[0]:
    i=i+n
    n=n+1
    a[0][i-1]=i

for i in a[1]:
    i=i+n2
    n2=n2+1
    a[1][x]=i
    x=x+1
    
    
print(a)
