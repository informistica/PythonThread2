"""
In questo caso, i processi sono consapevoli l'uno dell'altro e possono comunicare direttamente.
Esempio: Comunicazione diretta. I processi comunicano utilizzando messaggi diretti 
o altri meccanismi di comunicazione. 
Ad esempio, uno scenario di scambio di dati tra server e client 
o tra processi all'interno di un'applicazione che utilizza canali di comunicazione diretti.
"""
import os
import multiprocessing
from multiprocessing import Process, Pipe

def process_id():
    print("Server PID: %s, Process Name: %s " % (
        os.getpid(),
        multiprocessing.current_process().name)
    )
           
def process_function(conn):
    process_id()
    print("Elaboro il dato ricevuto ed invio il risultato")
    # Operazioni che richiedono la comunicazione diretta
    data_received = conn.recv()  # Riceve dati dal processo genitore
    result = data_received * 2   # Esegue un'operazione sui dati ricevuti
    conn.send(result)            # Invia il risultato al processo genitore
    conn.close()                 # Chiude la connessione

if __name__ == "__main__":
    process_id()
    print("Creo una connessione e un processo figlio")
    # Creazione di una connessione Pipe per la comunicazione bidirezionale tra processi
    # restituisce due oggetti di connessione
    parent_conn, child_conn = Pipe()

    # Dato da inviare al processo figlio
    data = 5

    # Creazione di un nuovo processo, che sarà il figlio
    p = Process(target=process_function, args=(child_conn,))
    p.start()

    # Invio dei dati al processo figlio attraverso la connessione
    parent_conn.send(data)

    # Ricezione del risultato dal processo figlio
    result = parent_conn.recv()

    # Attendi il completamento del processo figlio
    p.join()
    process_id()
    print("Stampo il risultato ricevuto")
    
    # Stampa del risultato
    print(result)
