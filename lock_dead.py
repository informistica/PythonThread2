import threading
import time
# Definizione delle risorse
resource_a = threading.Lock()
resource_b = threading.Lock()

# Funzione per l'esecuzione del primo thread
def thread_1():
    # Acquisizione del lock sulla risorsa A
    resource_a.acquire()
    print("Thread 1 ha acquisito il lock sulla risorsa A")
    # Tentativo di acquisizione del lock sulla risorsa B
    print("Thread 1 tenta di acquisire il lock sulla risorsa B")
    resource_b.acquire()
    print("Thread 1 ha acquisito il lock sulla risorsa B")
    # Rilascio delle risorse
    resource_b.release()
    resource_a.release()
  
    

# Funzione per l'esecuzione del secondo thread
def thread_2():
    # Acquisizione del lock sulla risorsa B
    resource_b.acquire()
    print("Thread 2 ha acquisito il lock sulla risorsa B")
    # Tentativo di acquisizione del lock sulla risorsa A
    print("Thread 2 tenta di acquisire il lock sulla risorsa A")
    resource_a.acquire()
    print("Thread 2 ha acquisito il lock sulla risorsa A")
    # Rilascio delle risorse
    resource_a.release()
    resource_b.release()
    

# Creazione dei thread
thread1 = threading.Thread(target=thread_1)
thread2 = threading.Thread(target=thread_2)
# Avvio dei thread
thread1.start()
thread2.start()
# Attesa che i thread terminino
thread1.join()
thread2.join()

print("Fine del programma")