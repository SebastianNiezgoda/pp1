x=int(input('Podaj twój wzrost w cm\n'))
#1 stopa 30,48cm
#1 cal to 2,54 cm

stopy=(x//30.48)
stopynacm=(stopy*30.48)
z=(x-stopynacm)
cale=(z/2.54)

print(f'Twoj wzrost to {x} cm, lub {stopy} stóp i {cale} cali')

