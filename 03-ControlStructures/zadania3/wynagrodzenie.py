#Podaj liczbę godzin: 45
#Podaj stawkę godzinową: 10
#Wynagrodzenie: 475.0

def computepay(hours,rate):
    if hours>40:
        wynagrodzenie=rate*1.5*hours
    else:
        wynagrodzenie=rate*hours
    return wynagrodzenie

print(computepay(20,10))
        