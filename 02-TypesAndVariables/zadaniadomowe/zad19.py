x=float(input('podaj twój wzrost w metrach\n'))
y=int(input('podaj twoją wage\n'))

#BMI obliczamy dzieląc masę ciała (w kilogramach) przez wzrost do kwadratu (w metrach).#

BMI=(y/x**2)

print(f'twoja waga to{y} kg, twój wzrost to {x} metra, a twój wskaźnik bmi to {BMI} ')