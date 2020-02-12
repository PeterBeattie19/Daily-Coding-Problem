class Stack:
    def __init__(self):
        self._stack = [] 

    def pop(self):
        if len(self._stack) != 0:
            return self._stack.pop(-1) 
    
    def push(self, item):
        self._stack.append(item) 

    def is_empty(self):
        return len(self._stack) == 0 


class Queue:
    def __init__(self):
        self._stack_1 = Stack() 
        self._stack_2 = Stack() 

    def enqueue(self, item):
        if self._stack_1.is_empty():
            self._stack_1.push(item)
        else:
            self._transfer_stack(self._stack_1, self._stack_2) 
            self._stack_2.push(item)
            self._transfer_stack(self._stack_2, self._stack_1) 
        
    def dequeue(self):
        if not self._stack_1.is_empty():
            return self._stack_1.pop()  

    def is_empty(self):
        return self._stack_1.is_empty() 

    @staticmethod
    def _transfer_stack(st1, st2):
        while not st1.is_empty():
            st2.push(st1.pop())
    

q = Queue()
for i in range(10):
    q.enqueue(i) 

while not q.is_empty():
    print(q.dequeue()) 
