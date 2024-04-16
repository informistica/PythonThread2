"""
Un deadlock si verifica quando due o più processi/thread rimangono bloccati 
indefinitamente in attesa che l'altro rilasci una risorsa che hanno acquisito. 
Questo può verificarsi quando i processi acquisiscono le risorse in un ordine 
non corretto.
In questo esempio, due thread tentano di acquisire due lock in ordine diverso. 
Ciò può portare a un deadlock in cui entrambi i processi rimangono bloccati indefinitamente.
"""
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    lock1.acquire()
    print("Thread 1 ha acquisito la risorsa 1")
    time.sleep(1)
    lock2.acquire()
    print("Thread 1 ha acquisito la risorsa 2")
    lock2.release()
    print("Thread 1 ha rilasciato la risorsa 2")
    lock1.release()
    print("Thread 1 ha rilasciato la risorsa 1")
    print("Thread 1 termina")

def thread2():
    lock2.acquire()
    print("Thread 2 ha acquisito la risorsa 2")
    lock1.acquire()
    print("Thread 2 ha acquisito la risorsa 1")
    lock1.release()
    print("Thread 2 ha rilasciato la risorsa 1")
    lock2.release()
    print("Thread 2 ha rilasciato la risorsa 2")
    print("Thread 2 termina")

if __name__ == "__main__":
    thread1 = threading.Thread(target=thread1)
    thread2 = threading.Thread(target=thread2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
