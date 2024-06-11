import queue
data = queue.Queue()
data.put('test')
data.put(1)
print(data.qsize())
print(data.get())
print(data.qsize())
print(data.get())
print(data.qsize())
