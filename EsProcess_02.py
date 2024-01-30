"""
L’esempio seguente ci mostra in modo molto semplice il funzionamento 
della funzione fork, ottenendo da terminale il pid dei processi parent 
e child
"""
import os

print(f"PID parent {os.getpid()}")
pid = os.fork()
print(f"PID child {pid}")
 
