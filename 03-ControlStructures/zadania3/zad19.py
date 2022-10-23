#For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years.
wiek=float(input("podaj wiek psa w latach ludzkich"))
l=(wiek*10.5)
y=(wiek-2)*4
z=2*10.5
if wiek>2:
    print(f"wiek w latach psich:{z+y}")
elif wiek<2:
    print(f'wiek w latach psich:{l}')
else:
    print(f'wiek w latach psich {z}')


