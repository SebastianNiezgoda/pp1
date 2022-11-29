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

print()

for col in range(len(a[1])):
    temp=a[0][col]
    a[0][col]=a[4][col]
    a[4][col]=temp

for i in a:
    for j in i:
        print(j,end=" ")
    print()