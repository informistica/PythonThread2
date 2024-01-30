from time import perf_counter
import os

def create(filename, id):
    print(f'{id} Writing the file {filename}')
    content=str(id)

    # utilizzo 
    with open(filename, 'w') as f:
        f.write(content)

def read(filename,id):
    print(f'{id} Reading the file {filename}')
    # utilizzo 
    with open(filename, 'r') as f:
        content = f.read()
        print(content)

def delete(filename,id):
    print(f'{id} Removing the file {filename}')
    os.remove(filename)

def main():
    filenames = [
        'C:/temp/test0.txt',
        'C:/temp/test1.txt',
        'C:/temp/test2.txt',
        'C:/temp/test3.txt',
        'C:/temp/test4.txt',
        'C:/temp/test5.txt',
        'C:/temp/test6.txt',
        'C:/temp/test7.txt',
        'C:/temp/test8.txt',
        'C:/temp/test9.txt',
        'C:/temp/test10.txt',
    ]

    for i,filename in enumerate(filenames):
        create(filename, i)
    for i,filename in enumerate(filenames):
        read(filename, i)
    for i,filename in enumerate(filenames):
        delete(filename, i)


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
    #It took 0.16 second(s) to complete.
    #The following program has the same functionality. However, it uses multiple threads instead: