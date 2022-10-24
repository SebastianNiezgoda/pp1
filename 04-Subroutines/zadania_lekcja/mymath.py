from random import Random, random
from secrets import choice
from tkinter import Y


def read_number():
    x=int(input("Podaj liczbę"))
    return x

def generate_number():
    y=choice(range(0,10))
    return y




for i in range(999999):
    
    if read_number()==generate_number():
        print(f"Gratulacje wygrałeś")
        break
    else:
        print("Nie trafiłeś, spróbuj ponownie")

        