#Scrivi un programma parallelo che esegua la seguente espressione matematica: 
# z=[(3+4)*(5+2)*(3*3)]/2
import multiprocessing

def calculate_partial_result(queue,data):
    partial_result = eval(data)
    queue.put(partial_result)

if __name__ == "__main__":
    # Crea una coda per memorizzare i risultati parziali
    result_queue = multiprocessing.Queue()

    # Crea due processi per calcolare i risultati parziali
    process1 = multiprocessing.Process(target=calculate_partial_result, args=(result_queue,"3+4"))
    process2 = multiprocessing.Process(target=calculate_partial_result, args=(result_queue,"5+2"))
    process3 = multiprocessing.Process(target=calculate_partial_result, args=(result_queue,"3*3"))

    # Avvia i processi
    process1.start()
    process2.start()
    process3.start()

    # Attendi che i processi completino
    process1.join()
    process2.join()
    process3.join()

    # Prendi i risultati parziali dalla coda e calcola il risultato finale
    partial_result1 = result_queue.get()
    partial_result2 = result_queue.get()
    partial_result3 = result_queue.get()
    print(partial_result1,partial_result2,partial_result3)
    final_result = (partial_result1*partial_result2*partial_result3)/2

    # Stampa il risultato finale
    print("Il risultato final       e è:", final_result)
