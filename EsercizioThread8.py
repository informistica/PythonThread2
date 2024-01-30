import os
import time
import threading
import multiprocessing
 
NUM_WORKERS = 10
 
def only_sleep():
    """ Do nothing, wait for a timer to expire """
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
    )
    time.sleep(1)
 
 
def crunch_numbers():
    """ Do some computations """
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
    )
    x = 0
    while x < 10000000:
        x += 1

if __name__ == "__main__":
    ## Run tasks serially
    """
    start_time = time.time()
    for _ in range(NUM_WORKERS):
        crunch_numbers()
    end_time = time.time()
    
    print("Serial time=", end_time - start_time)
    """
    # Run tasks using threads
    start_time = time.time()
    threads = [threading.Thread(target=crunch_numbers) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()
    
    print("Threads time=", end_time - start_time)
    """
    # Run tasks using processes
    start_time = time.time()
    processes = [multiprocessing.Process(target=crunch_numbers) for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]
    [process.join() for process in processes]
    end_time = time.time()
    
    print("Parallel time=", end_time - start_time)
    """