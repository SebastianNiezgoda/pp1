
n1=5
n2=2
n3=1
z=int(input('Podaj kwote w zł'))

x=z//n1
reszta5=z%n1
y=reszta5//n2
reszta2=reszta5%n2
l=reszta2

print(f'5zł-{x}')
print(f'2zł-{y}')
print(f'1zł-{l}')

