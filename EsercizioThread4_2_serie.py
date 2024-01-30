"""
"""

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
    print(f"{task_name} -> {action_name}: FINE in {action_time_end - action_time_start }")

def task(task_name):
    task_time_start = datetime.datetime.now()
    #print(f"Task: {task_name} partito: {datetime.datetime.now()}, durata: {arg}")
    print(f"\nTASK: {task_name} PARTITO")
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name)
    )
    if task_name == '1.Preparare il condimento':
        action(task_name,"1.Taglia cipolla",1)
        action(task_name,"2.Soffrigere cipolla",3)
        action(task_name,"3.Taglia pomodori",1)
        action(task_name,"4.Aggiungere pomodori alla cipolla e cuocere per 10 minuti",5)
    elif task_name=='2.Fare bollire acqua':
        action(task_name,"1.Riempire la pentola",1)
        action(task_name,"2.Metterla sul fuoco per 10 minuti",5)
    elif task_name=='3.Mettere a cuocere la pasta':
        action(task_name,"1.Aggiungere il sale nell'acqua",1)
        action(task_name,"2.Aggiungere la pasta nella pentola e cuocere per 8 minuti",3)
    elif task_name=='4.Consumare la pasta':
        action(task_name,"1.Scolare",1)
        action(task_name,"2.Condire la pasta con il condimento",2)
        action(task_name,"3.Servire in tavola",1)
          
    task_time_end = datetime.datetime.now()
    #time.sleep(arg)
    print(f"{task_time_start} \n{task_time_end } \n{task_time_end - task_time_start } TASK: {task_name} TERMINATO")

if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("***SERIE")
    task("1.Preparare il condimento")
    task("2.Fare bollire acqua")
    task("3.Mettere a cuocere la pasta")
    task("4.Consumare la pasta")

    time_end = datetime.datetime.now()
    print(f"Il primo è pronto in {time_end - time_start}")

