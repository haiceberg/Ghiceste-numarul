import random

print(""" 
Bine ai venit!
Acest joc este de tipul 'Ghicește numărul' în care
calculatorul se gândește la un număr, iar tu afli dacă
numărul pe care îl introduci este sau nu cel la care calculatorul
s-a gândit.
""")

numar_ghicit = random.randint(0,50)
sanse = 5
numaratoare = 0 

while numaratoare < sanse:
    numaratoare += 1
    nr_meu = int(input('Introdu numarul: '))
    
    if nr_meu == numar_ghicit:
        print(f'Felicitari! Ai ghicit numarul din {numaratoare} incercari.')
        break

    elif numaratoare >= sanse:
        print(f'Imi pare rau! Numarul era {numar_ghicit} si ti-ai mai si risipit incercarile... Data viitoare.')
    
    elif nr_meu > numar_ghicit:
        print(f'Numarul {nr_meu} este mai mare decat numarul la care ma gandesc.')
    
    elif nr_meu < numar_ghicit:
        print(f'Numarul {nr_meu} este mai mic decat numarul la care ma gandesc.')
