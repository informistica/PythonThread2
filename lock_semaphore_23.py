import queue
import threading
import time

# Creazione di una coda con dimensione massima di 3 elementi
q = queue.Queue(maxsize=3)

# Funzione per inserire elementi nella coda
def producer():
    i=0
    while True:
        i+=1
        print(f"Produttore sta cercando di inserire {i} nella coda...")
        try:
            q.put(i, block=True, timeout=2)  # Inserimento con timeout di 2 secondi
            print(f"Produttore ha inserito {i} nella coda.")
        except queue.Full:
            print("La coda è piena, impossibile inserire. Saltando l'inserimento.")
            time.sleep(1)  # Attendi un secondo prima di riprovare l'inserimento

# Funzione per rimuovere elementi dalla coda
def consumer():
    while True:
        time.sleep(1)  # Aggiungi un ritardo prima di ogni tentativo di prelievo
        print("Consumatore sta cercando di prelevare un elemento dalla coda...")
        try:
            item = q.get(block=True, timeout=2)  # Rimozione con timeout di 2 secondi
            print(f"Consumatore ha prelevato {item} dalla coda.")
        except queue.Empty:
            print("La coda è vuota, impossibile prelevare.")

# Creazione dei thread per il produttore e il consumatore
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Avvio dei thread
producer_thread.start()
consumer_thread.start()

# Attendi il completamento dei thread
producer_thread.join()
consumer_thread.join()

print("Fine del programma.")
