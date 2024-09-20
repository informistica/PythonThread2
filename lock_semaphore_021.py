import threading
import time
import random
from queue import Queue

# Coda condivisa per l'immagazzinamento dei dati prodotti
buffer = Queue(maxsize=5)

# Semaforo per controllare l'accesso al buffer
buffer_semaphore = threading.Semaphore(1)



# Funzione per il produttore
def producer(producer_id):
    while True:
        # Genera un dato casuale
        data = random.randint(1, 100)
        
        # Acquisisce il semaforo per accedere al buffer
        buffer_semaphore.acquire()
        try:
            # Inserisce il dato nel buffer
            buffer.put(data,block=True, timeout=2)
            print(f"Produttore {producer_id} ha prodotto il dato {data} [num elem nella  coda {buffer.qsize()}]")
            
            # Rilascia il semaforo del buffer
            buffer_semaphore.release()
            
            # Attendi un po' prima di produrre un altro dato
            time.sleep(random.uniform(0.5, 1.5))
        except :
            print("La coda è piena, impossibile inserire. Salto l'inserimento.")
            time.sleep(random.uniform(0.5, 1.5))
            pass

# Funzione per il consumatore
def consumer(consumer_id):
    while True:

        # Acquisisce il semaforo per accedere al buffer
        buffer_semaphore.acquire()
        
        # Preleva un dato dal buffer
        data = buffer.get()
        print(f"Consumatore {consumer_id} ha consumato il dato {data} [num elem nella  coda {buffer.qsize()} ]")
        
        # Rilascia il semaforo del buffer
        buffer_semaphore.release()
        
        # Attendi un po' prima di consumare un altro dato
        time.sleep(random.uniform(0.5, 1.5))

# Creazione di produttori e consumatori
producers = []
consumers = []

for i in range(3):
    p = threading.Thread(target=producer, args=(i,))
    producers.append(p)

for i in range(2):
    c = threading.Thread(target=consumer, args=(i,))
    consumers.append(c)

# Avvio dei thread
for p in producers:
    p.start()

for c in consumers:
    c.start()

# Attendiamo la terminazione dei thread
for p in producers:
    p.join()

for c in consumers:
    c.join()

print("Fine del programma.")


"""
put(item[, block[, timeout]]): Aggiunge un elemento alla coda. Se la coda è piena, il comportamento dipende dall'argomento block. Se block è True (il valore predefinito), il metodo attende finché non c'è spazio disponibile nella coda. Se block è False, viene sollevata un'eccezione queue.Full se la coda è piena. L'argomento opzionale timeout specifica il tempo massimo di attesa (in secondi) per l'operazione di inserimento.
get([block[, timeout]]): Rimuove e restituisce un elemento dalla coda. Se la coda è vuota, il comportamento dipende dall'argomento block. Se block è True (il valore predefinito), il metodo attende finché non ci sono elementi disponibili nella coda. Se block è False, viene sollevata un'eccezione queue.Empty se la coda è vuota. L'argomento opzionale timeout specifica il tempo massimo di attesa (in secondi) per l'operazione di rimozione.
empty(): Restituisce True se la coda è vuota, False altrimenti.
full(): Restituisce True se la coda è piena, False altrimenti.
qsize(): Restituisce il numero di elementi presenti nella coda.
put_nowait(item): Equivalente a put(item, False).
get_nowait(): Equivalente a get(False).
join(): Blocca il thread chiamante finché tutti gli elementi presenti nella coda non vengono elaborati. Questo metodo è utile in combinazione con il threading per aspettare il completamento di tutti i task inseriti nella coda.

"""