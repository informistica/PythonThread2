from concurrent.futures import ThreadPoolExecutor
from time import sleep

def count_number_of_words(sentence):
    number_of_words = len(sentence.split())
    sleep(1)
    print("Number of words in the sentence :"+ str(number_of_words))

def count_number_of_characters(sentence):
    number_of_characters = len(sentence)
    sleep(1)
    print("Number of characters in the sentence :" + number_of_characters)

if __name__ == '__main__':

    sentence = "Python Multiprocessing is an important library for achieving parallel programming."
    executor = ThreadPoolExecutor(4)

    thread1 = executor.submit(count_number_of_words, (sentence))
    thread2 = executor.submit(count_number_of_characters, (sentence))

    sleep(1)
    print("Thread 1 executed ? :",thread1.done())
    print("Thread 2 executed ? :",thread2.done())
