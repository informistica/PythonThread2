import queue
import threading
import time
import random

# Creazione di una coda con dimensione massima di 3 elementi
buffer = queue.Queue(maxsize=3)

# Semaforo per controllare l'accesso al buffer
buffer_semaphore = threading.Semaphore(1)
# Funzione per inserire elementi nella coda
def producer():
    for i in range(5):
        print(f"Produttore sta cercando di inserire {i} nella coda...")
        buffer_semaphore.acquire()
        try:
            buffer.put(i, block=True, timeout=2)  # Inserimento con timeout di 2 secondi
            print(f"Produttore ha inserito {i} nella coda.")
        except queue.Full:
            print("La coda è piena, impossibile inserire. Saltando l'inserimento.")
            # Attendi un po' prima di produrre un altro dato
            time.sleep(random.uniform(0.5, 1.5))
        finally:
            buffer_semaphore.release()

# Funzione per rimuovere elementi dalla coda
def consumer():
    while True:
        time.sleep(1)  # Attendi un secondo
        print("Consumatore sta cercando di prelevare un elemento dalla coda...")
        buffer_semaphore.acquire()
        try:
            item = buffer.get(block=True, timeout=2)  # Rimozione con timeout di 2 secondi
            print(f"Consumatore ha prelevato {item} dalla coda. [num elem nella  coda {buffer.qsize()}]")
        except queue.Empty:
            print("La coda è vuota, impossibile prelevare.")
            # Attendi un po' prima di consumare un altro dato
            time.sleep(random.uniform(0.5, 1.5))
        finally:
            buffer_semaphore.release()

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
