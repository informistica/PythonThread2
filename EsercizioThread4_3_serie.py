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
    if task_name == '1.Mettere la tovaglia':
        action(task_name,"1.Prendere tovaglia dal cassetto",1)
        action(task_name,"2.Aprire e mettere sul tavolo",3)
    elif task_name=='2.Mettere piatto':
        action(task_name,"1.Prendere piatto dallo scolapiatti",1)
        action(task_name,"2.Appoggiare piatto sul tavolo",1)
    elif task_name=='3.Prendere le posate':
        action(task_name,"1.Prendere forchetta dal cassetto",1)
        action(task_name,"2.Appoggiare forchetta sul tavolo",1)
    elif task_name=='4.Prendere tovaiolo':
        action(task_name,"1.Prendere tovaiolo dal cassetto",1)
        action(task_name,"2.Appoggiare tovaiolo sul tavolo",1)
          
    task_time_end = datetime.datetime.now()
    #time.sleep(arg)
    print(f"{task_time_start} \n{task_time_end } \n{task_time_end - task_time_start } TASK: {task_name} TERMINATO")

if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("***SERIE")
    task("1.Mettere la tovaglia")
    task("2.Mettere piatto")
    task("3.Prendere le posate")
    task("4.Prendere tovaiolo")

    time_end = datetime.datetime.now()
    print(f"La tavola è stata apparecchiata in: {time_end - time_start}")

