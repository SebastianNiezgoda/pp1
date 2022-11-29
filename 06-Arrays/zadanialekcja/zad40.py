ar=[
[-38, 19],
[5,40],
[-7,11],
[29,16]
] 
a=ar[0][0]


for rows in range(len(ar)):
    for col in range(len(ar[0])):
        if ar[rows][col]<a:
            x=ar[rows][col]
            r=rows
            r2=col
        else:
            x=ar[0][0]
            r=0
            r2=0
z=ar[0][0]
for rows in range(len(ar)):
    for col in range(len(ar[0])):
        if ar[rows][col]>z:
            z=ar[rows][col]
            r3=rows
            r4=col

print(f'Najwieksza liczba to {z},jej współrzedne to {r3},{r4}, a najmniejsza to {x} jej wspolrzedne to {r},{r2}')
            

        
print(x)

