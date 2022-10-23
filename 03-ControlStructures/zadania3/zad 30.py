from unittest import skip


y=int(input("podaj liczbe"))
for x in range(0,y+1):
    if x%2==0:
        skip
    elif x%3==0:
        skip
    elif x%5==0:
        skip
    else:
        print(x)