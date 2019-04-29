from random import randint
from time import sleep
from queue import Queue
from myThread import  MyThread

def writeQ(queue):
    print('生产对象问...')
    queue.put('xxx', 1)
    print("现在的尺寸", queue.qsize())

def readQ(queue):
    val = queue.get(1)
    print('计算对象从问…现在的尺寸', \
          queue.qsize())

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('全部完成')

if __name__ =='__main__':
    main()