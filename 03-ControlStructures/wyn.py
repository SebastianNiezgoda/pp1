x=int(input('podaj liczbe godzin\n'))
y=int(input('podaj stawke godzinową\n'))
if x>=40 :
    z=(x*(y*1.5))
else:
    z=(x*y)

print(f'Liczba godzin:...{x}\n') 
print(f'stawka godzinowa...{y}\n')
print(f'Wypłata:{z}\n')   