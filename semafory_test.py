from threading import Semaphore, Thread
import time

semA = Semaphore(0)
semB = Semaphore(0)
semC = Semaphore(0)
#CABCB

def printA(ntimes):
    for i in range(ntimes):
        semC.release()
        semA.acquire()
        print('A ', end="")
        semB.release()
        semB.release()
        semA.acquire()
        semC.release()
        semA.acquire()
        semB.release()
        semB.release()
        semA.acquire()
        #time.sleep(1)


def printB(ntimes):
    for i in range(ntimes):
        semB.acquire()
        semB.acquire()
        print('B ', end="")
        semA.release()
        #time.sleep(1)
        


def printC(ntimes):
    for i in range(ntimes):
        semC.acquire()
        print('C ', end="")
        semA.release()
        
        #time.sleep(1)
       

how_many = 5
threads = []
threads.append(Thread(target=printA, args=(how_many,)))
threads.append(Thread(target=printB, args=(2*how_many,)))
threads.append(Thread(target=printC, args=(2*how_many,)))

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("\nAll done")