#%%
# Tutaj będzie główny kod gry.

PlanszaDoGry = {'7':' ','8':' ','9':' ',
                '4':' ','5':' ','6':' ',
                '1':' ','2':' ','3':' ',
                }

KlawiszeGry = []

for i in PlanszaDoGry:
    KlawiszeGry.append(i)
print(KlawiszeGry)

#def DrukujPlansze():
 #   print('  '+'|'+'  '+'|'+'  ')
 #   print('--+--+--')
 #   print('  '+'|'+'  '+'|'+'  ')
 #   print('--+--+--')
 #   print('  '+'|'+'  '+'|'+'  ')
    
def DrukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")
    


#DrukujPlansze(PlanszaDoGry)

def gra():

    gracz = 'X'
    licznik = 0


    for licznik in range(10):
        DrukujPlansze(PlanszaDoGry)
        move = input(f"To jest ruch gracza {gracz}. Wybierz, gdzie postawić znak!")
        if PlanszaDoGry[move] == ' ':
            PlanszaDoGry[move] = gracz
            licznik += 1
             
        else:
            print('Miesce zajęte.\n Wybierz wolne miejsce')
            continue
        


        if licznik >=  5:
    #poziome
            if PlanszaDoGry['7'] == PlanszaDoGry['8'] == PlanszaDoGry['9'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!\n')
                print(f'WYGRAŁ GRACZ: {gracz}')
                break

            elif PlanszaDoGry['4'] == PlanszaDoGry['5'] == PlanszaDoGry['6'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f"Wygrał gracz {gracz}")
                break

            elif PlanszaDoGry['1'] == PlanszaDoGry['2'] == PlanszaDoGry['3'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f"Wygrał gracz {gracz}")
                break

    #pionowe
            elif PlanszaDoGry['7'] == PlanszaDoGry['4'] == PlanszaDoGry['1'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f"Wygrał gracz {gracz}")
                break

            elif PlanszaDoGry['8'] == PlanszaDoGry['5'] == PlanszaDoGry['2'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f"Wygrał gracz {gracz}")
                break

            elif PlanszaDoGry['9'] == PlanszaDoGry['6'] == PlanszaDoGry['3'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f"Wygrał gracz {gracz}")
                break

        #przekątne
            elif PlanszaDoGry['9'] == PlanszaDoGry['5'] == PlanszaDoGry['1'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f"Wygrał gracz {gracz}")
                break

            elif PlanszaDoGry['7'] == PlanszaDoGry['5'] == PlanszaDoGry['3'] != ' ':
                DrukujPlansze(PlanszaDoGry)
                print('\nKoniec gry!\n')
                print(f"Wygrał gracz {gracz}")
                break

            if licznik == 9:
                print('\nKoniec Gry!\n')
                print('\nRemis!\n')
        if gracz == 'X':
            gracz = 'O'
        else:
            gracz = 'X'   

    restart = input('Czy chcesz zagrać jeszcze raz/ t /n')
    if restart == 't' or restart == 'T':
        for key in KlawiszeGry:
            PlanszaDoGry[key] =' '

        gra()

if __name__ == "__main__":
    gra()
# %%
