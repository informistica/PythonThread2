# utils.py
#https://code.tutsplus.com/it/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612
#https://docs.python-requests.org/en/master/

import time
import logging
import requests
import os
 
 
class WebsiteDownException(Exception):
    pass
 
 

def count_words(content,address):
    number_of_words = len(content.split())
    print("Number of words in home " + address+" : " + str(number_of_words))

def load_homepage(address, timeout=20):
    """
    
    """
    try:
        response = requests.head(address, timeout=timeout)
        r = requests.get(address)
        if response.status_code >= 400:
            logging.warning("Website %s returned status_code=%s" % (address, response.status_code))
            raise WebsiteDownException()
        [p1,p2]=address.split("//")  
        print(p2)
        [p3,p4]=p2.split(".")

        url=p3+".txt"
        file = open(url, "w")
        file.write(r.text)
        file.close()
        file = open(url, "r")
        count_words(file.read(),address)
        file.close()
        os.remove(url)

    except requests.exceptions.RequestException:
        logging.warning("Timeout expired for website %s" % address)
        raise WebsiteDownException()
         
 
def notify_owner(address):
    """ 
    Send the owner of the address a notification that their website is down 
     
    For now, we're just going to sleep for 0.5 seconds but this is where 
    you would send an email, push notification or text-message
    """
    logging.info("Notifying the owner of %s website" % address)
    time.sleep(0.5)
     
 

def manage_homepage(address):
    """
    Utility function: load and save home page and count word 
    """
    try:
        load_homepage(address)
    except WebsiteDownException:
        notify_owner(address)



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
    start_time = time.time()
 
    for address in WEBSITE_LIST:
        manage_homepage(address)
            
    end_time = time.time()        
    
    print("Time for Serial Squirrel: %ssecs" % (end_time - start_time))


