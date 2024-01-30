"""
Processi Totalmente Ignari:

In questo caso, i processi non sono consapevoli l'uno dell'altro 
e operano indipendentemente senza alcuna comunicazione diretta o scambio di informazioni.
Esempio: Parallelismo di dati. Supponiamo di avere un'immagine divisa in pixel. 
Ogni processo si occupa di elaborare i dati in un determinato set di pixel senza 
avere alcuna consapevolezza degli altri processi che elaborano gli altri pixel.
"""


from multiprocessing import Process

def process_function(data):
    # Operazioni indipendenti
    result = data * 2
    print(result)

if __name__ == "__main__":
    data_list = [1, 2, 3, 4]
    processes = []

    for data in data_list:
        p = Process(target=process_function, args=(data,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
