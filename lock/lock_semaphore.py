import threading

# Risorsa condivisa
resource = []  # Esempio: una lista che rappresenta le istanze della risorsa
resource_count = 3  # Numero totale di istanze della risorsa

# Semaforo per gestire l'accesso alla risorsa
semaphore = threading.Semaphore(resource_count)

# Funzione per l'accesso alla risorsa
def access_resource():
    semaphore.acquire()  # Acquisizione del semaforo per accedere alla risorsa
    # Sezione critica: utilizzo della risorsa
    resource.append("Nuova istanza")
    print("Risorsa accessibile. Numero di istanze disponibili:", len(resource))
    semaphore.release()  # Rilascio del semaforo per consentire ad altri thread di accedere alla risorsa

# Creazione dei thread
threads = []
for _ in range(5):
    t = threading.Thread(target=access_resource)
    threads.append(t)

# Avvio dei thread
for t in threads:
    t.start()

# Attesa che i thread terminino
for t in threads:
    t.join()

# Stampa delle istanze finali della risorsa
print("Istanze finali della risorsa:", resource)

"""
In questo esempio, utilizziamo un semaforo (semaphore) per gestire l'accesso alla risorsa (resource) 
che ha più istanze disponibili. Il semaforo è inizializzato con il numero totale di istanze della 
risorsa (resource_count).

Ogni thread richiede l'acquisizione del semaforo (semaphore.acquire()) prima di accedere alla risorsa. 
Nella sezione critica, il thread può utilizzare la risorsa come necessario. 
Nel nostro esempio, aggiungiamo una nuova istanza alla lista resource. 
Dopo aver completato l'accesso alla risorsa, il thread rilascia il semaforo (semaphore.release()) 
per consentire ad altri thread di accedere alla risorsa.
Il semaforo garantisce che solo un numero massimo di thread pari al numero di istanze disponibili 
possa accedere contemporaneamente alla risorsa. Gli altri thread che tentano di accedere alla 
risorsa quando tutte le istanze sono occupate verranno bloccati fino a quando una delle istanze 
non sarà rilasciata.Dopo che tutti i thread hanno completato l'accesso alla risorsa, 
viene stampato lo stato finale della risorsa (resource), che mostrerà tutte le istanze che sono state utilizzate dai thread.
"""