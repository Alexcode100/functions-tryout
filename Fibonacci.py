def fibonacci():
    Aantal=int(input('Geef het aantal keer dat je deze reeks wilt laten laten herhalen\n---> '))
    Pogingen = 0
    ReeksBegin = 0
    Reeks2eGetal = 1
    while True:
        if Aantal == Pogingen:
            break
        else:
            print(ReeksBegin)
            print(Reeks2eGetal)
            ReeksBegin = ReeksBegin + Reeks2eGetal
            Reeks2eGetal = ReeksBegin + Reeks2eGetal
            Pogingen = Pogingen + 1
fibonacci()