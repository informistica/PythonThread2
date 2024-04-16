import threading
import time

# Variabili condivise
vet_dati = [None] * 5  # Inizializzazione di una lista vuota di 5 elementi

vet_dati[0]=2
vet_dati[1]=5
vet_dati[2]=6
ultimo = 2  # Indice dell'ultimo elemento inserito nel vettore
print("vet_dati=",vet_dati)
print("ultimo=",ultimo)
# Funzione del produttore
def produttore():
    global ultimo
    ultimo += 1
    valore=10
    time.sleep(1)
    # Inserisce il valore nella posizione libera trovata
    vet_dati[ultimo] = valore
    # Stampa il vettore dopo l'inserimento
    print(f"Produttore: Inserito valore {valore} in posizione {ultimo} nel vettore: {vet_dati}")

# Funzione del consumatore
def consumatore():
    global ultimo
    # Legge l'ultimo valore inserito e lo azzera
    valore = vet_dati[ultimo]
    vet_dati[ultimo] = 0
    # Stampa il valore letto e il vettore dopo l'azzeramento
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
