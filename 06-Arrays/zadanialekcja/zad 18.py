ar=[15, 8, 31, 47, 2, 19]

print("array: ",end="")
for i in ar:
    print(i,end=" ")

print("\nśrednia:",end=" ")
suma=0
for i in ar:
    suma=suma+i
średnia=suma/len(ar)
print(średnia)
