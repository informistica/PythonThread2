import threading
import time

total_bytes = 0

def update_counter():
    global total_bytes
    for _ in range(1000):
        # SIMULAZIONE BUG: Leggiamo, aspettiamo un attimo e poi scriviamo
        # Questo aumenta drasticamente la probabilità di una race condition
        current = total_bytes
        time.sleep(0.0001) 
        total_bytes = current + 1

def start_challenge():
    global total_bytes
    total_bytes = 0
    threads = []
    for _ in range(5):
        t = threading.Thread(target=update_counter)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"Byte totali calcolati: {total_bytes} (Attesi: 5000)")

start_challenge()