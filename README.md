# multithreading_vs_multiprocessing_in_python
>> Conclusion :- for io_bound operations like data read/write to a remote server fetch is best to be done using threading , and due to GIL cpu bound process won't work with threading.

- A process is what we call a program that has been loaded into memory along with all the resources it needs to operate.
 It has its own memory space.

- A thread is the unit of execution within a process. A process can have multiple threads running as a part of it, 
where each thread uses the process’s memory space and shares it with other threads.

- Multithreading is a technique where multiple threads are spawned by a process to do different tasks, at about the same time,
 just one after the other. This gives you the illusion that the threads are running in parallel,
  but they are actually run in a concurrent manner.
   In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.

- Multiprocessing is a technique where parallelism in its truest form is achieved. Multiple processes are run across multiple CPU cores,
 which do not share the resources among them. Each process can have many threads running in its own memory space.
  In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.


- The Python Global Interpreter Lock or GIL, in simple words,
 is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter. 
This means that only one thread can be in a state of execution at any point in time.

--> SO THREAD IS USED FOR database fetch , write operations.

- NOTE :- threading doesn't work for CPU bound process.
Okay, we just proved that threading worked amazingly well for multiple IO-bound tasks.

` Let’s use the same approach for executing our CPU-bound tasks.
  Well, it did kick off our threads at the same time initially,
   but in the end, we see that the whole program execution took about a whopping 40 seconds! What just happened?
    This is because when Thread-1 started, it acquired the Global Interpreter Lock (GIL) which prevented Thread-2 to make use of the CPU.
     Hence, Thread-2 had to wait for Thread-1 to finish its task and release the lock so that it can acquire the lock and perform its task.
      This acquisition and release of the lock added overhead to the total execution time.
 Therefore, we can safely say that threading is not an ideal solution for tasks that requires CPU to work on something. 
 `
 
 
 
- Now that we got a fair idea about multiprocessing helping us achieve parallelism, we shall try to use this technique for running our IO-bound tasks. We do observe that the results are extraordinary, just as in the case of multithreading. Since the processes Process-1 and Process-2 are performing the task of asking their own CPU core to sit idle for a few seconds, we don’t find high Power Usage. But the creation of processes itself is a CPU heavy task and requires more time than the creation of threads. Also, processes require more resources than threads. Hence, it is always better to have multiprocessing as the second option for IO-bound tasks, with multithreading being the first. 
 

