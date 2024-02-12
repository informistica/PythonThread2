"""
2) Processi Indirettamente a Conoscenza Uno dell'Altro:

In questo caso, i processi potrebbero non conoscere direttamente gli altri, 
ma possono interagire attraverso uno scambio indiretto di informazioni, 
ad esempio, attraverso una struttura dati condivisa o un intermediario.
Esempio: Una coda condivisa. I processi possono mettere dati in una coda condivisa 
e prelevarli successivamente. Anche se i processi non conoscono direttamente gli altri processi, 
condividono una struttura dati (la coda) per scambiare informazioni.
"""

import os # il modulo fornisce funzionalità per interagire con il sistema operativo
from multiprocessing import Process, Queue,current_process
"""
-- Queue: classe che rappresenta una coda condivisa tra processi. 
È utilizzata per consentire la comunicazione tra processi, 
consentendo loro di scambiarsi dati in modo sicuro.
put(item): Aggiunge un elemento alla coda.
get(): Rimuove e restituisce un elemento dalla coda. 
empty(): Restituisce True se la coda è vuota, altrimenti restituisce False.
full(): Restituisce True se la coda è piena, altrimenti restituisce False.
qsize(): Restituisce il numero di elementi presenti nella coda.
close(): Chiude la coda. 
-- current_process:  funzione che restituisce un oggetto Process 
che rappresenta il processo in esecuzione.
"""

def process_id():
    print(f"Server PID: {os.getpid()}, Process Name: { current_process().name}, Process PID: { current_process().pid}")
  
           
def process_function(data, result_queue):
    process_id()
    print("Elabora: ",data)
    result = data * 2
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
        print(result)
        
