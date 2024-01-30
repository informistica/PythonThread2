import threading
#import urllib.request
import requests
import os
current_directory = os.path.dirname(__file__)
 

# Funzione per il download, l'analisi e il salvataggio dei file
def download_and_analyze(urls):
    try:
        url,file_name=urls
        response = requests.get(url)
        if response.status_code == 200:
            data=response.text
        else:
            data="Errore"
        
        lines = data.split('\n')
        file_size = len(lines)
        print(file_size)
        
        if file_size < 100:
            save_dir = os.path.join(current_directory, "small")
        elif 50 <= file_size <= 250:
            save_dir = os.path.join(current_directory, "medium")
        else:
            save_dir = os.path.join(current_directory, "large")
        file_path = os.path.join(save_dir, file_name)
        #apro il file per la scrittura di testo
        with open(file_path, 'w') as file:
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


 
# Percorso della directory corrente dello script
current_directory = os.path.dirname(__file__)

# Nomi delle cartelle
folder_names = ["small", "medium", "large"]

# Crea le cartelle se non esistono
for folder_name in folder_names:
    # Percorso completo per la directory
   
    folder_path = os.path.join(current_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)


# Creiamo un oggetto Thread per ogni download e analisi
threads = []
for url in urls:
    t = threading.Thread(target=download_and_analyze, args=(url,))
    threads.append(t)

# Avviamo i thread
for t in threads:
    t.start()

# Attendiamo che i thread terminino
for t in threads:
    t.join()

print("Download e analisi completati.")