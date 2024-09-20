import threading
import time

# Definisci una risorsa condivisa (contatore)
counter = 0

# Definisci un semaforo con un contatore iniziale di 1
semaphore = threading.Semaphore(value=1)

# Funzione eseguita da ciascun thread
def thread_function(thread_id):
    global counter

    for _ in range(3):
        # Acquisisci il semaforo
        semaphore.acquire()

        # Modifica la risorsa condivisa
        counter += 1
        print(f"Thread {thread_id}: Valore della risorsa: {counter}")

        # Rilascia il semaforo
        semaphore.release()

        # Simula un po' di lavoro
        time.sleep(0.1)

# Crea due thread
thread1 = threading.Thread(target=thread_function, args=(1,))
thread2 = threading.Thread(target=thread_function, args=(2,))

# Avvia i thread
thread1.start()
thread2.start()

# Attendi che entrambi i thread completino l'esecuzione
thread1.join()
thread2.join()

print("Esecuzione completata.")
