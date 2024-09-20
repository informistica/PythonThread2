import queue
import threading
import time

# Creazione di una coda con dimensione massima di 3 elementi
q = queue.Queue(maxsize=2)

# Funzione per inserire elementi nella coda
def producer():
    i=0
    while True:
        i+=1
        time.sleep(1)
        print(f"Produttore sta cercando di inserire {i} nella coda...")
        try:
            q.put(i, block=True, timeout=4)  # Inserimento con timeout di 2 secondi
            print(f"Produttore ha inserito {i} nella coda.[num elem nella coda {q.qsize()}]-> [{list(q.queue)}]")
        except queue.Full:
            print(f"La coda è piena, impossibile inserire. Salto l'inserimento. num elem nella coda {q.qsize()}]-> [{list(q.queue)}]")
            time.sleep(1)  # Attendi un secondo prima di riprovare l'inserimento

# Funzione per rimuovere elementi dalla coda
def consumer():
    while True:
        time.sleep(0.5)  # Aggiungi un ritardo prima di ogni tentativo di prelievo
        print("Consumatore sta cercando di prelevare un elemento dalla coda...")
        try:
            #item = q.get(block=True, timeout=2)  # Rimozione con timeout di 2 secondi
            item = q.get(block=False) 
            print(f"Consumatore ha prelevato {item} dalla coda. num elem nella coda {q.qsize()}]-> [{list(q.queue)}]")
        except queue.Empty:
            print("La coda è vuota, impossibile prelevare. Salto il prelievo.")

# Creazione dei thread per il produttore e il consumatore
producer_thread = threading.Thread(target=producer)
producer_thread2 = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Avvio dei thread
producer_thread.start()
consumer_thread.start()

# Attendi il completamento dei thread
producer_thread.join()
consumer_thread.join()

print("Fine del programma.")
