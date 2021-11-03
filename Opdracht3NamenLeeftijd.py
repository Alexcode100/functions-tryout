import os
def NamenLeeftijd():
    while True:
        Doorgaan = input('Wilt u nog een naam en leeftijd doorgeven? (Ja/Nee)\n---> ')

        if Doorgaan == "Ja":
            Naam = input('Wat is uw naam?\n---> ')
            os.system('cls')
            Leeftijd = input('Wat is uw leeftijd?\n---> ')
            os.system('cls')
            print('--------------------------------\nHallo '+ str(Naam)+', je leeftijd is '+ str(Leeftijd)+'\n--------------------------------')
        else:
            quit()
NamenLeeftijd()