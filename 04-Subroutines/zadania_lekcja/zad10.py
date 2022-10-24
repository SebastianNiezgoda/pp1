from asyncore import read
from re import X


def read_number():
    x=int(input("podaj liczbę  "))
    return x

sum=read_number()+read_number()
print(f"suma={sum}")
