#Gemaakt door:
#---------
#Alexander den Otter  -  (99067410)
#Joris Lubbers  -  (99067627)
#---------

#imports
import random
import sys
import os
#imports

#Variabelen prijzen
Gebruikersnaam = 0
NBedrag1 = 450
NBedrag2 = 825
NBedrag3 = 650
NBedrag4 = 800
NBedrag5 = 1125
NBedrag6 = 1550
NBedrag7 = 375
NBedrag8 = 550
NBedrag9 = 250
NBedrag10 = 475
NBedrag11 = 450
NBedrag12 = 675
NBedrag13 = 750
NBedrag14 = 900
NBedrag15 = 1350
NBedrag16 = 1725
NBedrag17 = 550
NBedrag18 = 700
NBedrag19 = 475
NBedrag20 = 825
totaal1 = 0
#Variabelen prijzen


#Welkom
def intro(totaal1,Gebruikersnaam):
    os.system('cls')
    print('----------------------------------------------------------------')
    print('\033[1mThe heist\033[0m')
    print('----------------------------------------------------------------')
    print('''Hallo! Vandaag ga jij proberen een telefoonwinkel te overvallen!\nJij gaat proberen een bepaalde waarde aan telefoons te stelen\nZWaardoor jij winst kan maken met jou overval!''')
    print('----------------------------------------------------------------')
    StartRegels(totaal1,Gebruikersnaam)
#Welkom


#Kies(Start/Regels)
def StartRegels(totaal1,Gebruikersnaam):
    StartOfRegels = input('(Typ \033[1m1\033[0m om te Starten!)\n(typ \033[1m2\033[0m voor de Uitleg!)\n---> ')
    os.system('cls')
    if StartOfRegels == "2":
            print('''--------------------------------------------------------------------------------------------------------------------------------\nJij gaat een Apple Store overvallen waarbij je gaat proberen een bepaalde waarde aan telefoons te stelen,
    Je kan steeds kiezen welke telefoon je wilt stelen, alleen de vraag is welke telefoon je steelt. De goedkopere? Of de duurdere?
    De keuze is aan jou. Bij een goedkope telefoon heb je minder beveiliging en dus minder kans dat het alarm afgaat als je hem steelt
    Bij de duurdere telefoon heb je meer beveiliging en dus meer kans dat het alarm afgaat. En dat de politie je oppakt.\nDus wees voorzichtig en kies verstandig!\n--------------------------------------------------------------------------------------------------------------------------------''')
    begrepen(totaal1,Gebruikersnaam)
#Kies(Start/Regels)





def begrepen(totaal1,Gebruikersnaam):
    Gebruikersnaam = input('\n\n\033[1mGebruikersnaam\033[0m: ')
    os.system('cls')
    begrepen1 = input('---------------------------------------\nJe bent binnengebroken bij de Apple Shop!\nJe moet 7500$ intotaal stelen.\n---------------------------------------\nTyp \033[1mbegrepen\033[0m om verder te gaan\n---> ')
    os.system('cls')
    if begrepen1 == "begrepen":
        Overval1(totaal1,Gebruikersnaam)




def Overval1(totaal1,Gebruikersnaam):
    Normal1 = input('---------------------------------------\nJe ziet een 450$ mobiel en een 825$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 450$ mobiel\nTyp \033[1m2\033[0m voor de 825$ mobiel\n---> ')

    chance = random.randint(1,100)
    if chance <= 5 and Normal1=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal1=="1":
        totaal1 += NBedrag1

    chance = random.randint(1,100)
    if chance <= 9 and Normal1 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal1=="2":
        totaal1 += NBedrag2

    os.system('cls')
    if Normal1 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    Overval2(totaal1,Gebruikersnaam)


def Overval2(totaal1,Gebruikersnaam):
    Normal2 = input('---------------------------------------\nJe ziet een 650$ mobiel en een 800$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 650$ mobiel\nTyp \033[1m2\033[0m voor de 800$ mobiel\n---> ')

    chance = random.randint(1,100)
    if chance <= 6 and Normal2=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal2=="1":
        totaal1 += NBedrag3

    chance = random.randint(1,100)
    if chance <= 8 and Normal2 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal2=="2":
        totaal1 += NBedrag4

    os.system('cls')
    if Normal2 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    Overval3(totaal1,Gebruikersnaam)


def Overval3(totaal1,Gebruikersnaam):
    Normal3 = input('---------------------------------------\nJe ziet een 1125$ mobiel en een 1550$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 1125$ mobiel\nTyp \033[1m2\033[0m voor de 1550$ mobiel\n---> ')

    chance = random.randint(1,100)
    if chance <= 12 and Normal3=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal3=="1":
        totaal1 += NBedrag5

    chance = random.randint(1,100)
    if chance <= 17 and Normal3 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal3=="2":
        totaal1 += NBedrag6
    #kanscode3


    #TotaalBedrag3
    os.system('cls')
    if Normal3 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    #TotaalBedrag3
    Overval4(totaal1,Gebruikersnaam)


def Overval4(totaal1,Gebruikersnaam):
    #Overval4
    Normal4 = input('---------------------------------------\nJe ziet een 375$ mobiel en een 550$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 375$ mobiel\nTyp \033[1m2\033[0m voor de 550$ mobiel\n---> ')
    #Overval4

    #kanscode4
    chance = random.randint(1,100)
    if chance <= 3 and Normal4=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal4=="1":
        totaal1 += NBedrag7

    chance = random.randint(1,100)
    if chance <= 5 and Normal4 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal4=="2":
        totaal1 += NBedrag8
    #kanscode4


    #TotaalBedrag4
    os.system('cls')
    if Normal4 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    #TotaalBedrag4
    Overval5(totaal1,Gebruikersnaam)

def Overval5(totaal1,Gebruikersnaam):
    #Overval5
    Normal5 = input('---------------------------------------\nJe ziet een 250$ mobiel en een 475$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 250$ mobiel\nTyp \033[1m2\033[0m voor de 475$ mobiel\n---> ')
    #Overval5


    #kanscode5
    chance = random.randint(1,100)
    if chance <= 2 and Normal5=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal5=="1":
        totaal1 += NBedrag9

    chance = random.randint(1,100)
    if chance <= 4 and Normal5 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal5=="2":
        totaal1 += NBedrag10
    #kanscode5


    #TotaalBedrag5
    os.system('cls')
    if Normal5 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    #TotaalBedrag5
    Overval6(totaal1,Gebruikersnaam)


def Overval6(totaal1,Gebruikersnaam):
    #Overval6
    Normal6 = input('---------------------------------------\nJe ziet een 450$ mobiel en een 675$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 450$ mobiel\nTyp \033[1m2\033[0m voor de 675$ mobiel\n---> ')
    #Overval6


    #kanscode6
    chance = random.randint(1,100)
    if chance <= 4 and Normal6=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal6=="1":
        totaal1 += NBedrag11

    chance = random.randint(1,100)
    if chance <= 6 and Normal6 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal6=="2":
        totaal1 += NBedrag12
    #kanscode6


    #TotaalBedrag6
    os.system('cls')
    if Normal6 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    #TotaalBedrag6
    Overval7(totaal1,Gebruikersnaam)

def Overval7(totaal1,Gebruikersnaam):
    #Overval7
    Normal7 = input('---------------------------------------\nJe ziet een 750$ mobiel en een 900$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 750$ mobiel\nTyp \033[1m2\033[0m voor de 900$ mobiel\n---> ')
    #Overval7


    #kanscode7
    chance = random.randint(1,100)
    if chance <= 8 and Normal7=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal7=="1":
        totaal1 += NBedrag13

    chance = random.randint(1,100)
    if chance <= 10 and Normal7 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal7=="2":
        totaal1 += NBedrag14
    #kanscode7


    #TotaalBedrag7
    os.system('cls')
    if Normal7 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    #TotaalBedrag8
    Overval8(totaal1,Gebruikersnaam)

def Overval8(totaal1,Gebruikersnaam):
    #Overval8
    Normal8 = input('---------------------------------------\nJe ziet een 1350$ mobiel en een 1725$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 1350$ mobiel\nTyp \033[1m2\033[0m voor de 1725$ mobiel\n---> ')
    #Overval8


    #kanscode8
    chance = random.randint(1,100)
    if chance <= 12 and Normal8=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal8=="1":
        totaal1 += NBedrag15

    chance = random.randint(1,100)
    if chance <= 20 and Normal8 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal8=="2":
        totaal1 += NBedrag16
    #kanscode8


    #TotaalBedrag8
    os.system('cls')
    if Normal8 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    #TotaalBedrag8
    Overval9(totaal1,Gebruikersnaam)

def Overval9(totaal1,Gebruikersnaam):
    #Overval9
    Normal9 = input('---------------------------------------\nJe ziet een 550$ mobiel en een 700$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 475$ mobiel\nTyp \033[1m2\033[0m voor de 700$ mobiel\n---> ')
    #Overval9


    #kanscode9
    chance = random.randint(1,100)
    if chance <= 5 and Normal9=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal9=="1":
        totaal1 += NBedrag17

    chance = random.randint(1,100)
    if chance <= 7 and Normal9 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal9=="2":
        totaal1 += NBedrag18
    #kanscode9


    #TotaalBedrag9
    os.system('cls')
    if Normal9 == "1":
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    else:
        print('U heeft nu '+ str(totaal1)+'$ aan waarde gestolen! ')
    #TotaalBedrag9
    Overval10(totaal1,Gebruikersnaam)

def Overval10(totaal1,Gebruikersnaam):

    #Overval10
    Normal10 = input('---------------------------------------\nJe ziet een 475$ mobiel en een 825$ mobiel\nWelke pak je?\n---------------------------------------\nTyp \033[1m1\033[0m voor de 475$ mobiel\nTyp \033[1m2\033[0m voor de 825$ mobiel\n---> ')
    #Overval10


    #kanscode10
    chance = random.randint(1,100)
    if chance <= 4 and Normal10=="1":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal10=="1":
        totaal1 += NBedrag19

    chance = random.randint(1,100)
    if chance <= 8 and Normal10 == "2":
        print("Het alarm is afgegaan, de politie heeft je opgepakt!")
        sys.exit()
    elif Normal10=="2":
        totaal1 += NBedrag20
    #kanscode10


    #Einde2
    os.system('cls')
    if totaal1 >= 7500:
        print('------------------\nGoed gedaan '+ str(Gebruikersnaam)+'!\nJe hebt '+ str(totaal1) +'$ aan waarde gestolen.\nJe hebt \033[1mWINST\033[0m gemaakt met de overval!\n------------------')
    else:
        print('------------------\nHelaas ' + str(Gebruikersnaam) +'...\nJe hebt ' + str(totaal1)+'$ aan waarde gestolen.\nJe hebt \033[1mVERLIES\033[0m gemaakt en dus was alles voor niks!\n------------------')
    #Einde2

intro(totaal1,Gebruikersnaam)