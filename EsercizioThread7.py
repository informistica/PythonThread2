from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep


def tac_char(arg):
    myChar=arg
    if myChar=='A':
        numeroCarattere=1
    elif myChar=='B':
        numeroCarattere = 2
    elif myChar=='C':
        numeroCarattere = 3
    return numeroCarattere


if __name__ == '__main__':
  char='A'
  executor = ThreadPoolExecutor(1)
  thread1 = executor.submit(tac_char, (char))
  num1=thread1.result()
  sleep(2)
  print("Thread 1 terminato")
  print("Numero restituito : " + str(num1))