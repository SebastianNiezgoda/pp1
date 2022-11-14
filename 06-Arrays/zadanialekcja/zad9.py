arr=["Genowefa","Onufry","Celestyna",'Alojzy','Pankracy']
l=0
for x in range(len(arr)):
    y=len(arr[x])
    if y>l:
        l=y
        z=arr[x]
print(f"Najdłuższe imię= {z}")

