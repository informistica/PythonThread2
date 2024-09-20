import os
"""
Possiamo differenziare il comportamento del programma a seconda se ci troviamo 
nel processo child o parent e lo possiamo fare sfruttando appunto il valore 
restituito da fork().
"""
print("Avviato processo:")
pid = os.fork()
print(pid)
if pid > 0:
    print(f"Eseguo parent process {os.getpid()}")
else:
    print(f"Eseguo child process {os.getpid()}")