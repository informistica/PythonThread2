import os
import time
import threading
import multiprocessing
 
NUM_WORKERS = 4
 
def log_info():
  print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
    )

def only_sleep():
    """ Non fa nulla, aspetta lo scadere del timer per terminare """
    log_info()
    time.sleep(1)
 
def crunch_numbers():
    # Esegue dei calcoli
    log_info()
    x = 0
    while x < 100000000:
        x += 1
 

if __name__ == "__main__":
    ## Esegue i task in serie
    start_time = time.time()
    for _ in range(NUM_WORKERS):
        #only_sleep()
        crunch_numbers()
    end_time = time.time()
    print("Serial time=", end_time - start_time)
    
    # Esegue i task usando i threads
    start_time = time.time()
    #threads = [threading.Thread(target=only_sleep) for _ in range(NUM_WORKERS)]
    threads = [threading.Thread(target=crunch_numbers) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()
    print("Threads time=", end_time - start_time)
    
    # Esegue i task usando i processes
    start_time = time.time()
    #processes = [multiprocessing.Process(target=only_sleep) for _ in range(NUM_WORKERS)]
    processes = [multiprocessing.Process(target=crunch_numbers) for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    end_time = time.time()
    print("Parallel time=", end_time - start_time)