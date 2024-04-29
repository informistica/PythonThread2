import threading
import time

# Definizione di un semaforo con un valore iniziale di 1
semaphore = threading.Semaphore(1)

# Funzione per l'accesso alla risorsa condivisa
def access_resource(thread_id):
    print(f"Thread {thread_id} vuole accedere alla risorsa.")
    # Acquisizione del semaforo
    semaphore.acquire()
    print(f"Thread {thread_id} ha ottenuto l'accesso alla risorsa.")
    time.sleep(2)  # Simulazione di lavoro sulla risorsa
    print(f"Thread {thread_id} sta rilasciando la risorsa.")
    # Rilascio del semaforo
    semaphore.release()

# Creazione di alcuni thread che richiedono l'accesso alla risorsa
thread1 = threading.Thread(target=access_resource, args=(1,))
thread2 = threading.Thread(target=access_resource, args=(2,))

# Avvio dei thread
thread1.start()
thread2.start()

# Attendiamo la terminazione dei thread
thread1.join()
thread2.join()

print("Fine del programma.")
