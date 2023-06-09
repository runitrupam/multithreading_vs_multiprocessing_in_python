'''

A process is what we call a program that has been loaded into memory along with all the resources it needs to operate.
 It has its own memory space.

A thread is the unit of execution within a process. A process can have multiple threads running as a part of it, 
where each thread uses the process’s memory space and shares it with other threads.

Multithreading is a technique where multiple threads are spawned by a process to do different tasks, at about the same time,
 just one after the other. This gives you the illusion that the threads are running in parallel,
  but they are actually run in a concurrent manner.
   In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.

Multiprocessing is a technique where parallelism in its truest form is achieved. Multiple processes are run across multiple CPU cores,
 which do not share the resources among them. Each process can have many threads running in its own memory space.
  In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.


The Python Global Interpreter Lock or GIL, in simple words,
 is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter. 
This means that only one thread can be in a state of execution at any point in time.

--> SO THREAD IS USED FOR database fetch , write operations.

NOTE :- threading doesn't work for CPU bound process.
Okay, we just proved that threading worked amazingly well for multiple IO-bound tasks.

 Let’s use the same approach for executing our CPU-bound tasks.
  Well, it did kick off our threads at the same time initially,
   but in the end, we see that the whole program execution took about a whopping 40 seconds! What just happened?
    This is because when Thread-1 started, it acquired the Global Interpreter Lock (GIL) which prevented Thread-2 to make use of the CPU.
     Hence, Thread-2 had to wait for Thread-1 to finish its task and release the lock so that it can acquire the lock and perform its task.
      This acquisition and release of the lock added overhead to the total execution time.
 Therefore, we can safely say that threading is not an ideal solution for tasks that requires CPU to work on something. 

'''

import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

COUNT = 200000000
SLEEP = 10


def io_bound(sec):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} \
		---> Start sleeping...")
    time.sleep(sec)
    print(f"{pid} * {processName} * {threadName} \
		---> Finished sleeping...")


def cpu_bound(n):
    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(f"{pid} * {processName} * {threadName} \
		---> Start counting...")

    while n > 0:
        n -= 1

    print(f"{pid} * {processName} * {threadName} \
		---> Finished counting...")


if __name__ == "__main__":
    start = time.time()

    '''
    # Code snippet for Part 1
    io_bound(SLEEP)
    io_bound(SLEEP) # Takes 20 sec overall
    
    
    # Code snippet for Part 2. thread
    t1 = Thread(target = io_bound, args = (SLEEP,))
    t2 = Thread(target = io_bound, args = (SLEEP,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    # Code snippet for Part 2. process
    p1 = Process(target = io_bound, args = (SLEEP,))
    p2 = Process(target = io_bound, args = (SLEEP,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    
    # Code snippet for Part 3
    cpu_bound(COUNT)
    cpu_bound(COUNT) # 18sec
    
    
    # Code snippet for Part 4
    t1 = Thread(target = cpu_bound, args = (COUNT,))
    t2 = Thread(target = cpu_bound, args = (COUNT,))
    t1.start()
    t2.start()
    t1.join() # GIL stops parallel execution of threads.
    t2.join() # 17sec Therefore, we can safely say that threading is not an ideal solution for tasks that requires CPU to work on something. 

    
    # Code snippet for Part 5 , cpu bound Process.
    p1 = Process(target = cpu_bound, args = (COUNT,))
    p2 = Process(target = cpu_bound, args = (COUNT,))
    p1.start()
    p2.start()
    p1.join()
    p2.join() # 9sec Each process runs in parallel, making use of separate CPU core and its own instance of the Python interpreter.
    # GIL ,is a Mutex which works only for threads.

    '''

    # Here process is also fast wrt cpu bound, but as creating a Process has a hige overhead on the system(more resources) 
    # go with threading concept.
    # Code snippet for Part 6 , PROCESS in io bound
    p1 = Process(target = io_bound, args = (SLEEP,))
    p2 = Process(target = io_bound, args = (SLEEP,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # 39166 * Process - 1 * MainThread - --> Start sleeping...
    # 39167 * Process - 2 * MainThread - --> Start sleeping...
    # 39166 * Process - 1 * MainThread - --> Finished sleeping...
    # 39167 * Process - 2 * MainThread - --> Finished sleeping...
    # Time taken in seconds - 10.016791105270386 current_thread().name MainThread

    end = time.time()
    print('Time taken in seconds -', end - start, 'current_thread().name', current_thread().name)
