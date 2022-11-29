n=int(input("podaj liczbe: "))
arr=[1,2,3,4,5,6,7,8,9]
suma=0
for i in arr:
    if i>n:
        suma=suma+1

print(suma)