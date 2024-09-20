"""
Race Conditions:
Le race conditions si verificano quando il comportamento del programma dipende 
dall'ordine di esecuzione delle istruzioni tra più thread o processi. 
Questo può portare a risultati imprevisti o inconsistenti.
In questo esempio, due thread tentano di incrementare e decrementare una variabile 
counter contemporaneamente.  A causa della non atomicità delle operazioni di incremento
e decremento, si verifica una race condition che può portare a un valore finale 
imprevisto di counter.
"""
import threading
import time
from random import randint
counter = 0

def increment():
    global counter
    time.sleep(randint(0,1))
    for _ in range(10):
        
        counter += 1

def decrement():
    global counter
    for _ in range(10):
        counter -= 1

if __name__ == "__main__":
    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=decrement)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Counter:", counter)
