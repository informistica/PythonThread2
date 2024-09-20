"""
La starvation si verifica quando un thread/processo rimane in attesa indefinitamente 
di risorse  a causa della priorità data ad altri processi. 
Questo può accadere quando i processi vengono eseguiti in base a politiche di scheduling
non equamente. In questo esempio, due thread eseguono ciclicamente, ma se il thread 2 
ottenesse sempre la lock prima del thread 1, il thread 1 potrebbe essere affamato 
e non riuscire a eseguire il proprio lavoro.
In questo esempio, il timeout per il consumatore è stato impostato a 0.5 secondi, 
mentre il tempo di attesa tra la produzione di elementi da parte del produttore 
è stato impostato a 1 secondo. Questo significa che il consumatore potrebbe non essere
 in grado di ottenere gli elementi dalla coda con la stessa frequenza con cui vengono 
 prodotti, portando alla starvation.
"""
import threading
import queue
import time

def consumer():
    while True:
        try:
            item = q.get(timeout=0.5)  # Timeout più breve
            print(f"Consumatore ha ottenuto: {item}")
            time.sleep(2)  # Simula un'elaborazione lunga
            q.task_done()
        except queue.Empty:
            print("Nessun elemento disponibile, termina il consumatore")
            break

def producer():
    for i in range(5):
        print(f"Produttore produce: {i}")
        q.put(i)
        time.sleep(1)  # Tempo di attesa tra la produzione di elementi

if __name__ == "__main__":
    q = queue.Queue()

    # Avvio del consumatore
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()

    # Avvio del produttore
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    # Attendo il completamento del produttore
    producer_thread.join()

    # Attendo il completamento del consumatore
    q.join()
