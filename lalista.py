lista = []

def AggiungiLista(nome):
    lista.append(nome)

def VisualizzaLista():
    print("\n")
    for i in range(len(lista)):
        print(f"{i} : {lista[i]}")

def RimuoviElemento(indice):
    lista.pop(indice)

def Conta():
    print(f"\nCi sono {len(lista)} elementi")

def Svuota():
    lista.clear()

while True:
    print("\n0: Esci\n1: Aggiungi alla lista\n2: Visualizza lista\n3: Elimina elemento\n4: Conta elementi\n5: Azzera lista")
    try:
        x = int(input(""))
        if x == 0:
            break
        elif x == 1:
            AggiungiLista(input("\nInserire elemento da aggiungere: "))
        elif x == 2:
            VisualizzaLista()
        elif x == 3:
            RimuoviElemento(int(input("\nInserire indice dell'elemento da rimuovere: ")))
        elif x == 4:
            Conta()
        elif x == 5:
            Svuota()
    except:
        print("\nInput invalido")