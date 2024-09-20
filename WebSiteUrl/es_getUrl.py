from threading import Thread
from urllib.request import urlretrieve

def download_file(url, file_name):
    print(f"Inizio download di {file_name}...")
    urlretrieve(url, file_name) # scarica il file dal URL e salvalo con il nome specificato
    print(f"Download di {file_name} completato.")

# URL dei file da scaricare
urls = [ "http://elexpo.altervista.org/r.txt","https://jsonplaceholder.typicode.com/users", "https://jsonplaceholder.typicode.com/posts"]

# Creiamo un oggetto Thread per ogni file da scaricare
threads = []
for i, url in enumerate(urls):
    file_name = f"file{i+1}.txt"
    t = Thread(target=download_file, args=(url, file_name))
    threads.append(t)

# Avviamo i thread
for t in threads:
    t.start()

# Attendo che i thread terminino
for t in threads:
    t.join()

print("Download completati.")

