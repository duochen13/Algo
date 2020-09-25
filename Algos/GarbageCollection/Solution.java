

/*

Four Garbage Colectors
1. Serial: 
    All GC events are conducted serially in single thread, compaction is executed after each garbage collection
2. Parallel: 
    Multiple threads are used for minor GC, 
    Single thread is ued for major GC + Old Generation Compaction
3. CMS(Concurrent MArk Sweep):
   Multiple threads are used for minor garbage collection using the same algorithm as Parallel. Major garbage collection is multi-threaded, like Parallel Old, but CMS runs concurrently alongside application processes to minimize “stop the world” events (i.e. when the garbage collector running stops the application). No compaction is performed.
4. G1(Garbage First):
   

Garbage collection

Description:
When java programs run on JVM, objects are created on the heap, which is a portion of memory dedicated to the program.
The garbage collector finds these unused objects and deletes them to free up memory

Steps:
1. Unreferenced objs are identified and marked ready for garbage collection
2. Marked objs are deleted


HEAP
[young generation] [old generation] [permanent genration]

*/