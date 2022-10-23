from __future__ import barry_as_FLUFL


password=(8085)
for i in range(4):
    x=int(input("podaj hasło"))
    if x!=password:
        print("hasło niepoprawne")
    elif x==password:
        print("hasło poprawne")
        break
        
print("przepraszamy, karta została zablokowana")