 
import threading
import time

def thread(name,arg):
    print("Thread %s partito, ricevuto %d "% (name,arg))
    time.sleep(arg)
    print(f'Thread {name} terminato') 

if __name__ == "__main__":
    t1 = threading.Thread(target=thread, args=("DIN",1,))
    t2 = threading.Thread(target=thread, args=("DON",2,))
    t3 = threading.Thread(target=thread, args=("DAN",3,))
   
    t1.start() 
    t2.start() 
    t3.start()
   
    t1.join()
    t2.join()
    t3.join()
    print("Main terminato")

