import threading
a=0

def inc():
    global a
    a += 1

def call_inc():
    for _ in range(200000):
        inc()

def task():
    global a
    a = 0
    # creating the threads with the target as call_inc() function
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