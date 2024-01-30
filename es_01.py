from threading import Thread
import time
from random import randint

class IlMioThread (Thread):
   def __init__(self, suono, ritardo):
      Thread.__init__(self)
      self.suono = suono
      self.durata = ritardo
   def run(self):
      print ("Thread '" + self.suono + "' avviato")
      time.sleep(self.durata)
      print (self.suono)



val1=3
val2=2
val3=1

#thread1 = IlMioThread("DIN", randint(1,val1))
thread1 = IlMioThread("DIN", val1)
thread2 = IlMioThread("DON", val2)
thread3 = IlMioThread("DAN", val3)
# Avvio dei thread
thread1.start()
thread2.start()
thread3.start()
# Join
thread1.join()
thread2.join()
thread3.join()
# Fine dello script
print("Fine")