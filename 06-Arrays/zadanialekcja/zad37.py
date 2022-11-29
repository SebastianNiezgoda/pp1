ar=[[7, 3, 7, 9, 0],[2,9, 0, 1, 5],[3, 8, 6, 4, 7],[8 ,7 ,1, 1 ,5]]

for i in ar:
    for x in i:
        print(x,end=" ")
    print()
n=0
for i in range(0,4):
    n=n+ar[i][4]
print(n)
