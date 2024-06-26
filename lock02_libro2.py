import threading
import time

# Variabili condivise
vet_dati = [None] * 5  # Inizializzazione di una lista vuota di 5 elementi

vet_dati[0]=2
vet_dati[1]=5
vet_dati[2]=6
ultimo = 2   
print("vet_dati=",vet_dati)
print("ultimo=",ultimo)

def produttore():
    global ultimo
    ultimo += 1
    valore=10
    time.sleep(1)
    vet_dati[ultimo] = valore
    print(f"Produttore: Inserito valore {valore} in posizione {ultimo} nel vettore: {vet_dati}")


def consumatore():
    global ultimo
    valore = vet_dati[ultimo]
    vet_dati[ultimo] = 0
    print(f"Consumatore: Letto valore {valore} in posizione {ultimo} dal vettore: {vet_dati}")
    ultimo=ultimo-1
    time.sleep(1)  # Simula un'attesa prima di leggere un nuovo valore

# Avvio dei thread
produttore_thread = threading.Thread(target=produttore)
consumatore_thread = threading.Thread(target=consumatore)

produttore_thread.start()
consumatore_thread.start()

produttore_thread.join()
consumatore_thread.join()

print("Fine del programma")
