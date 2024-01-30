from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep


def generazione(arg):
  num=randint(1,arg)
  print ('generazione numero casuale da 1 a ' + str(arg))
  print('generato : ' + str(num) )
  return num


if __name__ == '__main__':
  uno=10
  due=20

  executor = ThreadPoolExecutor(1)

  thread1 = executor.submit(generazione, (uno))
  thread2 = executor.submit(generazione, (due))
 
  num1=thread1.result()
  num2 = thread2.result()
  sleep(2)
  if thread1.done() and thread2.done():
    print("Thread 1 terminato")
    print("Thread 2 terminato")
    print("La somma dei due numeri è : " + str(num1 + num2))