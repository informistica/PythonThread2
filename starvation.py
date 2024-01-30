import threading

# Funzione che simula un lavoro lungo
def long_running_task():
    thread_name = threading.current_thread().name
    print(f"{thread_name} inizia il lavoro.")
    while True:
        pass

# Creiamo una coda di thread
thread_queue = []

# Creiamo e avviamo 3 thread con priorità diversa
for i in range(3):
    thread = threading.Thread(target=long_running_task)
    thread.daemon = True  # Impostiamo i thread come daemon (priorità bassa)
    thread.start()
    thread_queue.append(thread)

# Avviamo un thread con priorità più alta
high_priority_thread = threading.Thread(target=long_running_task)
high_priority_thread.start()
thread_queue.append(high_priority_thread)

# Attendiamo che il thread con priorità più alta completi
high_priority_thread.join()

print("Il thread con priorità più alta ha completato il lavoro.")