"""
In questo esempio, il processo padre chiama os.fork() per creare un processo figlio. 
Dopo la chiamata a fork(), il processo figlio ha una copia esatta dello spazio di memoria del processo padre. 
Il processo figlio esegue la funzione child_process(), mentre il processo padre attende il completamento del processo figlio chiamando os.wait(). 
Quando il processo figlio termina, il processo padre riceve il PID del processo figlio terminato e lo stato di uscita.
"""
import os
import sys

def child_process():
    print("Sono il processo figlio con PID:", os.getpid())
    sys.exit(0)  # Termina il processo figlio con un codice di uscita 0

def main():
    print("Sono il processo padre con PID:", os.getpid())
    
    # Fork
    child_pid = os.fork()
    
    if child_pid == 0:
        # Siamo nel processo figlio
        child_process()
    else:
        # Siamo nel processo padre
        print("Processo figlio creato con PID:", child_pid)
        # Attendi il completamento del processo figlio
        _, status = os.wait()
        print("Processo figlio terminato con stato di uscita:", status)

if __name__ == "__main__":
    main()
