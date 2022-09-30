# Multi-threading and Multi-processing in Python
There are multiple libraries in Python which give the option to multi-thread and multi-process your code. This can give a significant speed improvement over single threaded code, allowing tasks to be completed in parallel, and in many cases doesn't require significantly more complicated code.

This repo contains two notebooks which give an introduction to the notion of multi-threading and multi-processing, examples of using high level code to process tasks more efficiently, and also an introduction to using lower level APIs to write a more controlled pipeline using a Computer Vision example.

The notebook **Intro_to_Mutli-Threading_and_Multi_Processing_in_Python.ipynb** gives an introduction (reproduced below) to threads and processes, and multiple examples of how the multiprocessing library can easyily be used to speed up your code. It also gives an example of using the **fast_map** library to combine threads and processes for even greater improvements.

The notebook **Low_Level_Mutli-Threading_and_Multi_Processing.ipynb** gives an example of spawning threads and processes directly, using multiple threads and processes simultaneously for different tasks in a Computer Vision use case.

## Introduction to threads and processes (from Intro_to_Mutli-Threading_and_Multi_Processing_in_Python.ipynb)

### The multi-threaded kitchen: understanding threads and processes

Imagine you were running a kitchen with 3 meal orders, what would be the most efficient way to cook the meals?

- Method 1 (_Single threaded_): Have a single chef follow the reciepe for each meal step by step. They start with the step of meal one, toasting some bread, then step two buttering it, and so on. Once meal one is finished they start with step one of meal two (boiling some water), then step two... until all three meals are cooked. This ensures the meals are cooked but is clearly a slow approach


- Method 2 (_Multi-threaded_): Have a single chef follow the reciepe for all three at the same time. Instead of doing each meal sequentially, they look for opportunities to pick up parts of each meal concurrently. So whilst waiting for the bread to toast in meal one step one, they start boiling the water for meal two step one, and chop the vegetables for meal three step one whilst waiting for both of those step to complete. Using opportunities to complete steps in each meal whilst waiting for steps in others to complete allows for the three meals to be cooked more quickly.


- Method 3 (_Multi-processed_): Have three chefs follow the reiepe for one of the meals each. Fully parallelise the cooking of each meal by having different chefs cook each meal at the same time. Chef 1 follows the reciepe for meal 1 step by step, chef 2 follows the reciepe for meal 2 step by step etc. This allows the three meals to be cooked at the same time and arrive more quickly


It is clear that method 1 would be a slow approach to completeing these meals, and methods 2 and 3 offer good ways to improve the efficiency of how the food is cooked.

Which out of method 2 and 3 is preferable will depend on the kind of meals being prepared:

- _I/O bound meals_: If each meal involves steps with long wait times (such as boiling water or waiting for something to roast), then method 2 can be a efficient as method 3: a single chef can likely efficiently handle all meals as well as multiple chefs. Even though they only do a single step of a reciepe at a time, due to the waiting times they can efficiently complete steps for all meals at the same time


- _cpu bound meals_: If each meal involves steps with lots of hands on tasks (lots of chopping and peeling for example) then method 3 will have an advanage over method 2: multiple chefs will be more efficient than a single chef. A single chef can only do one step at a time, so can only chop vegetables for meal two after finishing the chopping for meal one, whereas multiple chefs can chop for each meal simultaneously


Here method 2 represents multi-threading in Python: in this case a single cpu splits tasks into multiple threads. Even though it can only work on a single thread at a time, for some programs (those be described below as I/O bound) it will be the most efficient approach. 

Method 3 represented multi-processing in Python: in this case tasks are split over multiple cpus, which work on tasks in parallel. For some programs (those described below as cpu bound), this will be the most efficient approach.

### Some definitions

**Multi-threading**: The ability for a single cpu to provide multiple threads of execution concurrently. Processing power is increased by splitting a single processes in multiple threads.

**Multi-processing**: The ability for a system to use more than one cpu on parallel. Processing power is increased by using additional cpu cores to run multiple processes.

**Cpu bound**: a program is cpu bound if its speed of execution is limited by the speed of cpu. A quicker cpu would allow quicker exection of a cpu bound program. Programs that are computation heavy, such lots of mathematical calculations is likely to be cpu bound.

**I/O bound**: a program is I/O bound if its speed of execution is limited by input/output operations. The ability to more quickly read/write data to disk or recieve data from a server would allow quicker execution of an I/O bound program. Programs that involve writing or reading large objects to/from external servers are likely to be I/O bound.

As mentioned, multi-threading is like having a single chef work on multiple meals at once. If a program is I/O bound, a cpu can use waiting time on one thread to work on a different thread. Multi-processing is like having multiple chefs work on different meals: each chef can work on their meals at the same time.

### Some key differences

#### The GIL
A central difference between using threads and processes in Python comes down to the Global Interpreter Lock (GIL): the GIL means that only on thread in a process is ever executed at a time. So whilst a process might be split into multiple threads, Python will only be executing code in one thread at any time. Multi-processing is a way around the GIL, by splitting multiple processes over different cpus, threads on each of those cpus can be executed at the same time.

This has consequences for the type of programs that either addtional processes or threads are most effective for:
- multi-processing is likely to be most effective for a cpu bound program, as additional cpus can be used to execute computations in parallel. The GIL means that even using multiple threads, calcuations can only be executed in one thread at a time
- multi-threading is likely to be most effective for an I/O bound program, as multiple threads as the wait time for multiple I/O operations can be executed concurrently  

#### Memory
Multiple threads use the same memory space, so objects can be shared between threads more easily (similar to how a single chef has access to the same workspace). The downside to a shared memory space is the possibility of _race conditions_: as threads access the same objects, unexpected behaviour can happen if they are accessing and updating values at the same time. 

Multiple processes each have their own copies of objects in their own memory space. As a result, they avoid race conditions. On the downside, sharing objects is more complicated and there is more memory overhead involved with processes, partially meaning spawning new processes is slower than spawning new threads.
