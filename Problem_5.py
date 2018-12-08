def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(a,b):
    return a 
def cdr(a, b):
    return b 

print(cons(1,2)(car)) 