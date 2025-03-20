# Inizializzazione del saldo iniziale
saldo = 500  # Saldo iniziale

# Ciclo principale del programma
while True:
    # Menu principale
    print("\n Benvenuto nella tua banca!")
    print("1 Controlla il saldo")  # Opzione per controllare il saldo
    print("2 Deposita denaro")     # Opzione per depositare denaro
    print("3 Preleva denaro")      # Opzione per prelevare denaro
    print("4 Esci")                # Opzione per uscire dal programma

    # Input dell'utente per scegliere un'opzione
    scelta = input("Scegli un'opzione (1-4):")

    # Opzione 1: Controlla il saldo
    if scelta == "1":
        # Mostra il saldo attuale formattato con due decimali
        print(f"Il tuo saldo attuale è: {saldo: .2f}€")

    # Opzione 2: Deposita denaro
    elif scelta == "2":
        # Chiede all'utente quanto denaro vuole depositare
        deposito = float(input("Quanto vuoi depositare?"))
        if deposito > 0:  # Controlla che l'importo sia positivo
            saldo += deposito  # Aggiunge l'importo al saldo
            print(f"Deposito effettuato! Nuovo saldo: {saldo: .2f}€")
        else:
            # Messaggio di errore per importi non validi
            print("Inserisci un importo valido.")

    # Opzione 3: Preleva denaro
    elif scelta == "3":
        # Chiede all'utente quanto denaro vuole prelevare
        prelievo = float(input("Quanto vuoi prelevare?"))
        if prelievo > saldo:
            # Messaggio di errore se il saldo è insufficiente
            print("Saldo insufficiente!")
        elif prelievo <= 0:
            # Messaggio di errore per importi non validi
            print("Inserisci un importo valido.")
        else:
            # Sottrae l'importo dal saldo e conferma il prelievo
            saldo -= prelievo
            print(f"Prelievo effettuato! Nuovo saldo: {saldo: .2f}€")

    # Opzione 4: Esci
    elif scelta == "4":
        # Messaggio di saluto e uscita dal ciclo
        print("Grazie per aver utilizzato il servizio. Arrivederci!")
        break  # Interrompe il ciclo `while` e termina il programma

    # Gestione delle scelte non valide
    else:
        # Messaggio di errore per input non validi
        print("Scelta non valida. Inserisci un numero tra 1 e 4.")

# Funzione di saluto
def saluta():
    # Stampa un messaggio di benvenuto
    print("Ciao, benvenuto nel corso di Python!")

# Chiamata della funzione `saluta` per mostrare il messaggio di benvenuto
saluta()  # Output: Ciao, benvenuto nel corso di Python!