# classic queue one way queue
# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.


from queue import Queue

waitlist = Queue(maxsize=4)

print(waitlist.empty())
waitlist.put('Erin')
waitlist.put('Samantha')
waitlist.put('Joe')
waitlist.put('Martin')
waitlist.put('Helena')
print(waitlist.full())

print(waitlist.get())
print(waitlist.get())
print(waitlist.get())
print(waitlist.qsize())

print(waitlist.get())
print(waitlist.get_nowait())