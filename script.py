
saldo = 500 # Saldo iniziale

while True:
    print("\n Benvenuto nella tua banca!")
    print("1 Controlla il saldo")
    print("2 Deposita denaro")
    print("3 Preleva denaro")
    print("4 Esci")

    scelta = input("Scegli un'opzione (1-4):")

    if  scelta == "1":
        print(f"Il tuo saldo attuale è: {saldo: .2f}€")

    elif scelta == "2":
        deposito = float(input("Quanto vuoi depositare?"))
        if deposito > 0:
            saldo += deposito
            print(f"Deposito effettuato! Nuovo saldo: {saldo: .2f}€")
        else:
            print("Inserisci un importo valido.")

    elif scelta == "3":
        prelievo = float(input("Quanto vuoi prelevare?"))
        if prelievo > saldo:
            print("Saldo insufficiente!")
        elif prelievo <= 0:
            print("Inserisci un importo valido.")
        else:
            saldo -= prelievo
            print(f"Prelievo effettuato! Nuovo saldo: {saldo: .2f}€")

    elif scelta == "4":
        print("Grazie per aver utilizzato il servizio. Arrivederci!")
        break

    else:
        print("Scelta non valida. Inserisci un numero tra 1 e 4.")

def saluta():
    print("Ciao, benvenuto nel corso di Python!")

saluta() # Output: Ciao, benvenuto nel corso di Python!