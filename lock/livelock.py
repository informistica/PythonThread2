import threading

# Variabili per rappresentare due persone che cercano di fare spazio in una stanza
person1_lock = threading.Lock()
person2_lock = threading.Lock()

def person1():
    while True:
        print("Persona 1: Cerca di fare spazio.")
        person1_lock.acquire()
        print("Persona 1: Entra nella stanza.")
        person2_lock.acquire()
        print("Persona 1: Si ferma per far entrare Persona 2.")
        person2_lock.release()
        person1_lock.release()

def person2():
    while True:
        print("Persona 2: Cerca di fare spazio.")
        person2_lock.acquire()
        print("Persona 2: Entra nella stanza.")
        person1_lock.acquire()
        print("Persona 2: Si ferma per far entrare Persona 1.")
        person1_lock.release()
        person2_lock.release()

# Creiamo due thread che rappresentano le due persone
thread1 = threading.Thread(target=person1)
thread2 = threading.Thread(target=person2)

# Avviamo i thread
thread1.start()
thread2.start()