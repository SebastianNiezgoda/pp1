rows = 7
col=7
x=-6
count=0
z=1
for i in range(1, 8):
    for j in range(1,8):
        if count!=7:
            x=x+7
            count=count+1
            print(x,end=" ")
        else:
            count=1
            z=z+1
            x=0+z
            print(x,end=" ")
    print()
         
    