def pridat_novy_ukol():
    while(True):
        nazev = input('\nZadejte název úkolu: ')
        popis = input('Zadejte popis úkolu: ')
        if( len(nazev) != 0 and len(popis) != 0):
            ukol = {
                "nazev": nazev,
                "popis": popis
            }
            global ukoly
            ukoly.append(ukol)
            print("\nÚkol '",ukol["nazev"],"' byl přidán.",sep='')
            return
        else:
            print('\nNázev a/nebo popis nesmí být prázdný!')

def zobrazit_ukoly():
    global ukoly
    if( len(ukoly) == 0):
        print('\nSeznam úkolů je prázdný.')
        return False
    print('\nSeznam úkolů:')
    for k in range(len(ukoly)):
        ukol = ukoly[k]
        print(f'{k+1:4d}. {ukol["nazev"]:10} - {ukol["popis"]}')
    return True

def odstranit_ukol():
    if(not zobrazit_ukoly()):
        return
    index = input('\nZadejte číslo úkolu, který chcete odstranit: ')
    if( not index.isdigit()):
        print('\nNení zadáno číslo!')
        return
    index = int(index)
    global ukoly
    if( index > len(ukoly) or index <= 0):
        print('\nNeplatné číslo úkolu!')
        return

    ukol = ukoly[index-1]
    ukoly.pop(index - 1)
    print("\nÚkol '",ukol["nazev"],"' byl odstraněn.",sep='')

def hlavni_menu():
    while(True):
        print('\nSprávce úkolů - Hlavní menu')
        print('1. Přidat nový úkol')
        print('2. Zobrazit všechny úkoly')
        print('3. Odstranit úkol')
        print('4. Konec programu')
        volba = input('Zvolte možnost: ')

        if volba == "1":
            pridat_novy_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print('\nKonec programu.')
            return
        else:
            print('\nNeplatná možnost! Zkuste to znovu.')

ukoly = []
hlavni_menu()
