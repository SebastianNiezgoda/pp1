from secrets import choice


wyb=(1,2,3,4,5,6)
x=choice(wyb)
y=int(input("Podaj liczbe która wylosował komputer\n"))

print(x==y)