import threading
import time

# Definizione di un semaforo con un valore iniziale di 1
# consente solo a un singolo thread alla volta di acquisire il semaforo
# in questo caso equivale ad un lock()
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

"""
La classe Semaphore è utilizzata per la sincronizzazione tra thread.
 Un semaforo ha un valore intero che può essere usato per controllare l'accesso concorrente 
 a risorse condivise. Il valore del semaforo può essere positivo o zero. Se il valore è positivo, 
 indica il numero di thread che possono acquisire il semaforo senza essere bloccati. 
 Se il valore è zero, tutti i thread che cercano di acquisire il semaforo verranno bloccati 
 finché il valore del semaforo non diventa positivo.
 
 Metodi della classe:
 
 .acquire([blocking]): Acquisisce il semaforo. Se il parametro blocking è True (valore predefinito), 
 il thread viene bloccato finché il semaforo non viene acquisito. 
 Se è False e il semaforo non può essere acquisito immediatamente, 
 il metodo solleva un'eccezione BlockingIOError.

 .release(): Rilascia il semaforo. Incrementa il valore del semaforo e sblocca eventuali thread bloccati
in attesa di acquisire il semaforo.


"""