import threading

# Variabile condivisa
shared_data = 0

def thread1():
    global shared_data
    for i in range(1000000):
        shared_data += 1

def thread2():
    global shared_data
    for i in range(1000000):
        shared_data += 1

# Creiamo due oggetti Thread
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

# Avviamo i thread
t1.start()
t2.start()

# Attendo che i thread terminino
t1.join()
t2.join()

print(f"Valore finale di shared_data: {shared_data}")