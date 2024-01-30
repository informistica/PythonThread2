#https://www.tutorialexample.com/understand-python-thread-setdaemon-with-examples-create-a-daemon-thread-python-tutorial/
"""
creiamo un thread nel thread principale python,
il che significa che il thread main è il thread padre di questo thread.
"""
import threading
import time

def searchFiles(dir):
    print("start to search files in "+dir)
    for i in range(20):
        time.sleep(1)
        print("get file "+ str(i)+ " in "+ dir)
    print("search files end in "+ dir)

if __name__ == "__main__":
  search_thread = threading.Thread(target=searchFiles, args=["C:\\"])
  search_thread.start()
  print("main thread is started!")
  time.sleep(10)
  print("main thread is end!")
