#https://code.tutsplus.com/it/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612
#https://docs.python-requests.org/en/master/
# utils.py
 
import time
import logging
import requests

from queue import queue
from threading import Thread
import os
 
 
class WebsiteDownException(Exception):
    """
    Eventuale gestione dell'errore dovuto al sito che non risponde     
    """
          
 
def notify_owner(address):
    """ 
    Simuliamo l'invio di una email di notifica all'admin del sito che non risponde
    """
    logging.info("Notifying the owner of %s website" % address)
    time.sleep(0.5)


def count_words(content,address):
    number_of_words = len(content.split())
    print("Number of words in home " + address+" : " + str(number_of_words))

def load_homepage(address, timeout=20):
    """
    Carica l'home page del sito, crea un file, salva il contenuto, 
    lo ricarica dal file, conta le parole, chiude e rimuove il file
    """
    try:
        response = requests.head(address, timeout=timeout)
        r = requests.get(address)
        if response.status_code >= 400:
            logging.warning("Website %s returned status_code=%s" % (address, response.status_code))
            raise WebsiteDownException()
        [p1,p2]=address.split("//")  # da http://google.com
        [p3,p4]=p2.split(".") 
        url=p3+".txt"   # si ottiene google.txt
        file = open(url, "w")
        file.write(r.text)
        file.close()
        file = open(url, "r")
        count_words(file.read(),address)
        file.close()
        os.remove(url)
    except requests.exceptions.RequestException:
        logging.warning("Problem to get website %s" % address)
        raise WebsiteDownException()
            
 
def manage_homepage(address):
    """
    Utility function: load and save home page and count word 
    """
    try:
        load_homepage(address)
    except WebsiteDownException:
        notify_owner(address)

def worker():
    # Constantly check the queue for addresses
    while True:
        address = task_queue.get()
        manage_homepage(address)
        # Mark the processed task as done
        task_queue.task_done()

if __name__ == "__main__":
    WEBSITE_LIST = [
    'https://envato.com',
    'http://amazon.com',
    'http://facebook.com',
    'http://google.com',
    'http://google.fr',
    'http://google.es',
    'http://internet.org',
    'http://gmail.com',
    'http://stackoverflow.com',
    'http://github.com',
    'http://heroku.com',
    'http://really-cool-available-domain.com',
    'http://djangoproject.com',
    'http://rubyonrails.org',
    'http://basecamp.com',
    'http://trello.com',
    'http://yiiframework.com',
    'http://shopify.com',
    'http://another-really-interesting-domain.co',
    'http://airbnb.com',
    'http://instagram.com',
    'http://snapchat.com',
    'http://youtube.com',
    'http://baidu.com',
    'http://yahoo.com',
    'http://live.com',
    'http://linkedin.com',
    'http://yandex.ru',
    'http://netflix.com',
    'http://wordpress.com',
    'http://bing.com',
]

NUM_WORKERS = 4

task_queue = queue()

start_time = time.time()
        
# Create the worker threads
threads = [Thread(target=worker) for _ in range(NUM_WORKERS)]
 
# Add the websites to the task queue
[task_queue.put(item) for item in WEBSITE_LIST]
 
# Start all the workers
[thread.start() for thread in threads]
 
# Wait for all the tasks in the queue to be processed
task_queue.join()
 
         
end_time = time.time()        
 
print("Time for Threaded Squirrel: %ssecs" % (end_time - start_time))


