import sys
def PlusBerekening():
    GetalPlus1 = int(input('Voer het 1e getal in die je wilt optellen\n---> '))
    GetalPlus2 = int(input('Voer het 2e getal in die je wilt optellen\n---> '))
    Answer = GetalPlus1+GetalPlus2
    print(str(GetalPlus1) +' + '+ str(GetalPlus2) +' = '+ str(Answer))


def MinBerekening():
    GetalMin1 = int(input('Voer het 1e getal in die je wilt aftrekken\n---> '))
    GetalMin2 = int(input('Voer het 2e getal in die je wilt aftrekken\n---> '))
    Answer = GetalMin1-GetalMin2
    print(str(GetalMin1) +' - '+ str(GetalMin2) +' = '+ str(Answer))

def VermenigvuldigBerekening():
    GetalVermenigvuldig1 = int(input('Voer het 1e getal in die je wilt vermenigvuldigen\n---> '))
    GetalVermenigvuldig2 = int(input('Voer het 2e getal in die je wilt vermenigvuldigen\n---> '))
    Answer = GetalVermenigvuldig1*GetalVermenigvuldig2
    print(str(GetalVermenigvuldig1) +' x '+ str(GetalVermenigvuldig2) +' = '+ str(Answer))

def DelenBerekening():
    GetalDelen1 = int(input('Voer het 1e getal in die je wilt delen\n---> '))
    GetalDelen2 = int(input('Voer het 2e getal in die je wilt delen\n---> '))
    Answer = GetalDelen1/GetalDelen2
    print(str(GetalDelen1) +' ÷ '+ str(GetalDelen2) +' = '+ str(Answer))

Keuze = input('Typ 1 voor een optelberekening.\nTyp 2 voor een aftrekberekening.\nTyp 3 voor een vermenigvuldigberekening.\nTyp 4 voor een delenberekening.\n---> ')
if Keuze == "1":
    PlusBerekening()
elif Keuze == "2":
    MinBerekening() 
elif Keuze == "3":
    VermenigvuldigBerekening()
elif Keuze == "4":
    DelenBerekening()
else:
    exit()