 
import os
import time
import datetime 
import threading
import multiprocessing


def action(task_name,action_name,arg):
    action_time_start = datetime.datetime.now()
    #print(f"{task_name} -> {action_name} partito: {datetime.datetime.now()}, durata: {arg}")
    print(f"{task_name} -> {action_name}: INIZIO")
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
    )
    time.sleep(arg)
    action_time_end = datetime.datetime.now()
    #print(f"{task_name} -> {action_name} terminato in {action_time_end - action_time_start }")
    print(f"{task_name} -> {action_name}: FINE")

def task(task_name):
    task_time_start = datetime.datetime.now()
    #print(f"Task: {task_name} partito: {datetime.datetime.now()}, durata: {arg}")
    print(f"TASK: {task_name} PARTITO")
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
    )
    if task_name == '1.Prepara il condimento':
        a1 = threading.Thread(target=action, args=(task_name,"1.Taglia cipolla",1,))
        a1.start()
        a1.join()
        a2 = threading.Thread(target=action, args=(task_name,"2.Soffrigere cipolla",3,))
        a2.start()
        a3 = threading.Thread(target=action, args=(task_name,"3.Taglia pomodori",1,))
        a3.start()
        a2.join()
        a3.join()
        a4 = threading.Thread(target=action, args=(task_name,"4.Aggiungere pomodori alla cipolla e cuocere per 10 minuti",5,))
        a4.start()
        a4.join()
    elif task_name=='2.Fai bollire acqua':
        a1 = threading.Thread(target=action, args=(task_name,"1.Riempire la pentola",1,))
        a1.start()
        a1.join()
        a2 = threading.Thread(target=action, args=(task_name,"2.Metterla sul fuoco per 10 minuti",5,))
        a2.start()
        a2.join()
    elif task_name=='3.Metti a cuocere la pasta':
        a1 = threading.Thread(target=action, args=(task_name,"1.Aggiungere il sale nell'acqua",1,))
        a1.start()
        a1.join()
        a2 = threading.Thread(target=action, args=(task_name,"2.Aggiungere la pasta nella pentola e cuocere per 8 minuti",3,))
        a2.start()
        a2.join()
    elif task_name=='4.Consumare la pasta':
        a1 = threading.Thread(target=action, args=(task_name,"1.Scolare",1,))
        a1.start()
        a1.join()
        a2 = threading.Thread(target=action, args=(task_name,"2.Condire la pasta con il condimento",2,))
        a2.start()
        a2.join()
        a3 = threading.Thread(target=action, args=(task_name,"3.Servire in tavola",1,))
        a3.start()
        a3.join()

    task_time_end = datetime.datetime.now()
    #time.sleep(arg)
    print(f"{task_time_start} \n{task_time_end }\n{task_time_end - task_time_start } TASK: {task_name} TERMINATO\n")

if __name__ == "__main__":
    print("***MULTITHREADING")
    time_start = datetime.datetime.now()
    task1 = threading.Thread(target=task, args=("1.Prepara il condimento",))
    task2 = threading.Thread(target=task, args=("2.Fai bollire acqua",))
    task3 = threading.Thread(target=task, args=("3.Metti a cuocere la pasta",))
    task4 = threading.Thread(target=task, args=("4.Consumare la pasta",))
    task1.start() 
    task2.start() 
    task1.join()
    task2.join()
    task3.start()
    #time.sleep(5)
    task3.join()
    task4.start()
    task4.join()
    time_end = datetime.datetime.now()
    print(f"Il primo è pronto in {time_end - time_start}")

