"""
Esempio per illustrare come i semafori possono essere utilizzati per controllare l'accesso 
a un pool di risorse condivise in un ambiente concorrente.
"""

import threading
import time
import random

# Definizione di un semaforo con un valore iniziale di 5
semaphore = threading.Semaphore(5)

# Pool di risorse condivise
resource_pool = ["Risorsa 1", "Risorsa 2", "Risorsa 3", "Risorsa 4", "Risorsa 5"]

# Funzione per l'accesso alle risorse
def access_resource(thread_id):
    while True:
        # Acquisizione del semaforo
        semaphore.acquire()
        
        # Estrazione di una risorsa casuale dal pool
        resource = random.choice(resource_pool)
        resource_pool.remove(resource)
        
        print(f"Thread {thread_id} ha ottenuto l'accesso alla {resource}.")
        time.sleep(2)  # Simulazione di lavoro sulla risorsa
        print(f"Thread {thread_id} sta rilasciando la {resource}.")
        
        # Rilascio del semaforo
        semaphore.release()
        
        # Aggiunta della risorsa di nuovo al pool
        resource_pool.append(resource)
        
        # Attendi un po' prima di continuare
        time.sleep(random.uniform(0.5, 1.5))

# Creazione di alcuni thread che richiedono l'accesso alle risorse
threads = []
for i in range(10):
    t = threading.Thread(target=access_resource, args=(i,))
    threads.append(t)

# Avvio dei thread
for t in threads:
    t.start()

# Attendiamo la terminazione dei thread
for t in threads:
    t.join()

print("Fine del programma.")
"""
Abbiamo un pool di risorse condivise rappresentate da una lista chiamata resource_pool. 
Il semaforo è inizializzato con un valore di 5, indicando che massimo 5 thread possono accedere contemporaneamente alle risorse.
Ogni thread richiede l'accesso a una risorsa casuale dal pool utilizzando il semaforo. 
Una volta ottenuto l'accesso, il thread esegue un po' di lavoro sulla risorsa e poi rilascia il semaforo. 
Dopo aver rilasciato il semaforo, la risorsa viene nuovamente aggiunta al pool per consentire ad altri thread di accedervi.

"""