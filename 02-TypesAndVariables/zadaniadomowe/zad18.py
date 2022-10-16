from math import sqrt

#program liczacy pole trojkata

a=int(input("podaj pierwszy bok\n"))
b=int(input("podaj drugi bok\n"))
c=int(input("podaj trzeci bok\n"))

#p = (a + b + c)/2

p=((a+b+c)/2)

s=sqrt(p*(p-a)*(p-b)*(p-c))

print(f'Pole tego trójkata to {s}')