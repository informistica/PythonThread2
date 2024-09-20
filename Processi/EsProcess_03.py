# sleep is pre-emptive

import os
import time
import datetime 
import multiprocessing
 

 
def process1(start_time_p1):
    run_time_p1 = time.time()
    print(f"PID: {os.getpid()}, Processo 1 iniziato  {time.time()} dopo {(run_time_p1-start_time_p1)*1000} ms di attesa")
    #time.sleep(2)
    x = 0
    while x < 10000000:
        x += 1
    end_time_p2 = time.time()
    print(f"Processo 2 terminato in {end_time_p2-start_time_p2} sec.")
    end_time_p1 = time.time()
    print(f"Processo 1 finito in {end_time_p1-start_time_p1} sec.")
     
  
def process2(start_time_p2):
    run_time_p2 = time.time()
    print(f"PID: {os.getpid()}, Processo 2 Iniziato {time.time()} dopo {(run_time_p2-start_time_p2)*1000} ms di attesa")
    #time.sleep(2)
    x = 0
    while x < 10000000:
        x += 1
    end_time_p2 = time.time()
    print(f"Processo 2 terminato in {end_time_p2-start_time_p2} sec.")
     
    

if __name__ == "__main__":
    
    start_time_p1 = time.time()
    p1=multiprocessing.Process(target=process1,args=(start_time_p1,))
    print(f"Processo 1 start {time.time()}")
    p1.start()
    

    start_time_p2 = time.time()
    p2=multiprocessing.Process(target=process2,args=(start_time_p2,))
    print(f"Processo 2 start {time.time()}")
    p2.start()
    

    p1.join()
    p2.join()
    end_time_p2 = time.time()

    print(f"Terminati in {end_time_p2-start_time_p1} sec.")


 