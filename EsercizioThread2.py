from threading import Thread
import time,datetime



def thread1():
    print("Thread 1 iniziato")
    time.sleep(10)
    print("Thread 1 finito")
  
def thread2():
    print("Thread 2 iniziato")
    time.sleep(4)
    print("Thread 2 finito")


import multiprocessing
print("The number of cores in the system is",multiprocessing.cpu_count())
print("Main iniziato")
start_time = time.time()



t1 = Thread(target=thread1)
t2 = Thread(target=thread2)
t1.start()
t2.start()
t2.join()

t1.join()
#time.sleep(2)

#thread1()
#thread2()
end_time = time.time()

print(f"Main finito in {end_time-start_time}")