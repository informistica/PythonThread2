import threading
from queue import Queue
import time

def worker(queue):
    while True:
        item = queue.get()
        print("Processing item:", item)
        time.sleep(1)  # Simula il lavoro
        queue.task_done()

if __name__ == "__main__":
    queue = Queue()

    # Avvia il consumatore
    t = threading.Thread(target=worker, args=(queue,))
    t.start()

    # Aggiungi alcuni task alla coda
    for i in range(5):
        queue.put(i)

    # Aspetta che tutti i task siano completati
    queue.join()

    print("Tutti i task sono stati completati.")
