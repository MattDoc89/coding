# Questo è il mio secondo script
# By Matteo

# def calcola_area_triangolo (base, altezza):
    """
    Funzione che calcola l'area di un triangolo.
    """
    return (base * altezza) / 2

# Blocco try-except per evitare errori di input
try:
    base = float(input("Inserisci la base del triangolo: "))
    altezza = float(input("Inserisci l'altezza del triangolo: "))

    area = calcola_area_triangolo(base, altezza)
    print(f"L'area del triangolo è: {area: .2f}")
except ValueError:
    print("Errore: Devi inserire un numero valido!")