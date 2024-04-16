"""
2) Processi Indirettamente a Conoscenza Uno dell'Altro:

In questo caso, i processi potrebbero non conoscere direttamente gli altri, 
ma possono interagire attraverso uno scambio indiretto di informazioni, 
ad esempio, attraverso una struttura dati condivisa o un intermediario.
Esempio: Una coda condivisa. I processi possono mettere dati in una coda condivisa 
e prelevarli successivamente. Anche se i processi non conoscono direttamente gli altri processi, 
condividono una struttura dati (la coda) per scambiare informazioni.
"""
from multiprocessing import Process, Queue
import os
import multiprocessing

def process_id():
    print(f"Server PID: {os.getpid()}, Process Name: { current_process().name}, Process PID: { current_process().pid}")
  
           
def process_function(data, result_queue):
    process_id()
    print("Elabora: ",data)
    result = data * 2
    print("Inserisco in coda", result)
    result_queue.put(result)

if __name__ == "__main__":
    data_list = [1, 2, 3, 4]
    result_queue = Queue()
    processes = []

    for data in data_list:
        p = Process(target=process_function, args=(data, result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Il main stampa i risultati")
    while not result_queue.empty():
        result = result_queue.get()
        print("Prelevo dalla coda:")
        print(result)
        
