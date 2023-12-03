from threading import Semaphore, Thread

#global variables
A: int = 0
B: int = 0
C: int = 3

#define semaphores
#semNONAME = Semaphore(0)
#...
#SUMA 16
sem1 = Semaphore(0)
sem2 = Semaphore(0)
sem3 = Semaphore(0)
def threadP1():
    global A
    global B
    global C
    sem1.acquire()
    
    A = 10
    B = B + 5
    C = C + A
    print("Thread P1 is done...")

def threadP2():

    global A
    global B
    global C
    B = B + C
    sem2.release()
    sem1.acquire()
    A = A + B
    print("Thread P2 is done...")

def threadP3():

    global A
    global B
    global C
    sem2.acquire()
    C = B + 10
    sem3.release()
    sem1.acquire()
    A = 2 * A
    B = B + A
    print("Thread P3 is done...")

def threadP4():
    global A
    global B
    global C
    sem3.acquire()
    print("Sum result: ",A," + ",B," + ",C," = ",(A + B + C))
    print("Thread P4 is done...")
    sem1.release(3)

threads = []
threads.append(Thread(target=threadP1))
threads.append(Thread(target=threadP2))
threads.append(Thread(target=threadP3))
threads.append(Thread(target=threadP4))

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("All done")