a=[
[1,2,3],
[4,5,6],
[7,8,9],
[10,11,12],
[13,14,15]]

for i in a:
    for j in i:
        print(j,end=" ")
    print()

for row in range(len(a)):
    temp=a[row][0]
    a[row][0]=a[row][2]
    a[row][2]=temp

for i in a:
    for j in i:
        print(j,end=" ")
    print()