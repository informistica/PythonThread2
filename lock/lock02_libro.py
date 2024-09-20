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

def scarica():
    global tanti
    totS = tanti - 3
    time.sleep(randint(0,1))
    tanti = totS
def carica():
    global tanti
    totC = tanti + 5
    time.sleep(randint(0,1))
    tanti = totC
if __name__ == "__main__":
    thread1 = threading.Thread(target=carica)
    thread2 = threading.Thread(target=scarica)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Quanti?:", tanti)
