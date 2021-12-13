# *****************************************
# Multiprocessing in python

# multiprocessing = running task in parallel on different cpu cores, bypasses by GIL used for threading
                # multiprocessing = better for cpu bound task(heavy cpu usage)
                # multithreading = better for io bound task(waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count())

    a = Process(target=counter, args=(83333333,))
    b = Process(target=counter, args=(83333333,))
    c = Process(target=counter, args=(83333333,))
    d = Process(target=counter, args=(83333333,))
    a1 = Process(target=counter, args=(83333333,))
    b1 = Process(target=counter, args=(83333333,))
    c1 = Process(target=counter, args=(83333333,))
    d1 = Process(target=counter, args=(83333333,))
    a2 = Process(target=counter, args=(83333333,))
    b2 = Process(target=counter, args=(83333333,))
    c2 = Process(target=counter, args=(83333333,))
    d2 = Process(target=counter, args=(83333333,))

    a.start()
    b.start()
    c.start()
    d.start()
    a1.start()
    b1.start()
    c1.start()
    d1.start()
    a2.start()
    b2.start()
    c2.start()
    d2.start()

    a.join()
    b.join()
    c.join()
    d.join()
    a1.join()
    b1.join()
    c1.join()
    d1.join()
    a2.join()
    b2.join()
    c2.join()
    d2.join()
        
    print("Finished in: ", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()