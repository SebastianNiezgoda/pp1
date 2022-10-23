x=0

for x in range(0,31):
    y=x%3
    z=x%5
    if y==0:
        print("three")
    elif z==0:
        print("five")
    elif y==0 and z==0:
        print("bingo")
    else:
        print(x)
