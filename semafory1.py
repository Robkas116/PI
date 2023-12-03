from threading import Semaphore, Thread
import time

semA = Semaphore(1)
semB = Semaphore(2)
semC = Semaphore(0)
#BCAC

def printA(ntimes):
    for i in range(ntimes):
        semA.acquire()
        semA.acquire()
        print('A ', end="")
        semC.release()
        
        #time.sleep(1)
        


def printB(ntimes):
    for i in range(ntimes):
        semB.acquire()
        semB.acquire()
        print('B ', end="")
        #print(semA._value,semB._value,semC._value)
        semC.release()
        
       # time.sleep(1)
        


def printC(ntimes):
    for i in range(ntimes):
        semC.acquire()
        print('C ', end="")
        semA.release()
        semB.release()
        
        #time.sleep(1)
       

how_many = 5
threads = []
threads.append(Thread(target=printA, args=(how_many,)))
threads.append(Thread(target=printB, args=(how_many,)))
threads.append(Thread(target=printC, args=(2*how_many,)))

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("\nAll done")