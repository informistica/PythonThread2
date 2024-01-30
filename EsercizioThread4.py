 
import threading
import time

def thread1(arg):
    print("Thread DIN partito, ricevuto", arg)
    time.sleep(arg)
    print("Thread DIN terminato")

def thread2(arg):
    print("Thread DON partito, ricevuto", arg)
    time.sleep(arg)
    print("Thread DON terminato")

def thread3(arg):
    print("Thread DAN partito, ricevuto", arg)
    time.sleep(arg)
    print("Thread DAN terminato")

if __name__ == "__main__":

    t1 = threading.Thread(target=thread1, args=(1,))
    t2 = threading.Thread(target=thread2, args=(2,))
    t3 = threading.Thread(target=thread3, args=(3,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("Main terminato")

