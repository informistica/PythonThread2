import threading
a=0
def inc():
    # sezione critica:  avvengono operazioni su risorse condivise 
    # che devono essere eseguite in modo esclusivo da un solo thread alla volta.
    global a
    a += 1

def call_inc():
    for _ in range(200000):
        lock.acquire()
        inc()
        lock.release()

def task():
    global a
    a = 0
    #Creating a lock object
    global lock
    lock = threading.Lock() 
    # creating the threads with the target as call_inc() function and passing the lock object as argument
    trd1 = threading.Thread(target=call_inc)
    trd2 = threading.Thread(target=call_inc)
    # starting the threads
    trd1.start()
    trd2.start()
    # waiting til thread 1 is done with the execution
    trd1.join()
    trd2.join()

for i in range(5):
    task()
    print(f"Iteration {i} and the value of a = {a}")