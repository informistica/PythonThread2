"""
Abbiamo una risorsa condivisa (variabile a)
Eseguiamo due thread che per 5 volte incrementano una stessa variabile
per 200000 volte, il risultato che ci si aspetterebbe è 400000,
mentre in realtà l'esecuzione può produrre risultati diversi ad ogni esecuzione
a causa della race condition.
"""

from threading import Thread

def inc():
    global a
    a += 1

def call_inc():
    for _ in range(200000):
        inc()

def task():
    global a
    a = 0
    trd1 = Thread(target=call_inc)
    trd2 = Thread(target=call_inc)

    trd1.start()
    trd2.start()

    trd1.join()
    trd2.join()







for i in range(1):
    task()
    print(f"Iteration {i} and the value of a = {a}")