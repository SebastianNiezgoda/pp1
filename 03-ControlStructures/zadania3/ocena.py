def computegrade(wartość):
    if wartość >=0.9 and wartość<1:
        ocena=5.0
    elif wartość >=0.8 and wartość<0.9:
        ocena=4.5
    elif wartość >=0.7 and wartość<0.8:
        ocena=4
    elif wartość >=0.6 and wartość<0.7:
        ocena=3.5
    elif wartość>=0.5 and wartość<0.6:
        ocena =3
    elif wartość<0.5 and wartość>0:
        ocena=2
    else:
        print("nieprawidlowa wartość")
    return ocena


