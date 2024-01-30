import threading
import urllib.request
import requests
import os

# Funzione per il download, l'analisi e il salvataggio dei file
def download_and_analyze(urls, ok_word, save_dir_ok, save_dir_ko):
    try:
        url,file_name=urls
        response = urllib.request.urlopen(url)
        data = response.read()
        #file_name = url.split("/")[-1]
        #estrae l'ultimo elemento della lista ottenuta dalla suddivisione dell'URL in base a "/"

        if ok_word in data.decode("utf-8"):
            save_dir = save_dir_ok
        else:
            save_dir = save_dir_ko

        file_path = os.path.join(save_dir, file_name)

        with open(file_path, 'wb') as file:
            file.write(data)
        
        print(f"Download completato per {url} e salvato in {save_dir}")
    except Exception as e:
        print(f"Errore nel download di {url}: {str(e)}")

# Lista degli URL da scaricare
urls = [
    ("http://elexpo.altervista.org/r.txt", "file1.txt"),
    ("https://jsonplaceholder.typicode.com/users", "file2.txt"),
    ("https://jsonplaceholder.typicode.com/posts", "file3.txt")
]

# Parola scelta dall'utente
ok_word = "Python"

# Ottieni il percorso della directory corrente in cui si trova lo script
current_directory = os.path.dirname(__file__)
#Crea il percorso per creare la cartella
save_dir_ok = os.path.join(current_directory, "OK")
save_dir_ko = os.path.join(current_directory, "KO")
print(save_dir_ok)
# Cerca di creare la directory se non esiste, ma non genera un errore se esiste già.
os.makedirs(save_dir_ok, exist_ok=True)
os.makedirs(save_dir_ko, exist_ok=True)

# Creiamo un oggetto Thread per ogni download e analisi
threads = []
for url in urls:
    t = threading.Thread(target=download_and_analyze, args=(url, ok_word, save_dir_ok, save_dir_ko))
    threads.append(t)

# Avviamo i thread
for t in threads:
    t.start()

# Attendiamo che i thread terminino
for t in threads:
    t.join()

print("Download e analisi completati.")