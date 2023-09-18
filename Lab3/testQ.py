from linkedqueue import LinkedQueue
q = LinkedQueue()

q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
print(q)
def targetQueue(queue, target):
    run = True
    while run:
        try:
            if target == queue.peek():
                
                run = False
                
            if target != queue.peek():
                queue.dequeue()
        except:
            raise RuntimeError
        
targetQueue(q,0)

print(q.peek())

