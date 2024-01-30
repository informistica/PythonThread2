import threading
import time
 
def searchFiles(dir, wait = 1):
    print("start to search files in "+dir)
    for i in range(10):
        time.sleep(wait)
        print("get file "+ str(i)+ " in "+ dir)
    print("search files end in "+ dir)
    
def createThread():
    sub_thread = threading.Thread(target=searchFiles, args=["C:\\", 3])
    #sub_thread.setDaemon(True)
    sub_thread.start()
    searchFiles(dir="F:\\")

if __name__ == "__main__": 
  search_thread = threading.Thread(target=createThread)
  #search_thread.setDaemon(True)
  search_thread.start() 
  print("main thread is started!")
  time.sleep(5)
  print("main thread is end!")