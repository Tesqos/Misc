def sort_asc(x):
    from copy import deepcopy
    x=deepcopy(x)
    for n in range(len(x)):
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
    return x

def fib(n):
    prev, curr = 0, 1
    res=[]
    for i in range(n):
        res.append(prev + curr)
        prev, curr = curr, res[-1]
    return res

def ispaldr(s):"""Checks if argument is a palindrome."""
    if s==''.join([s[-i] for i in range(1,len(s)+1)]):
        return True
    else:
        return False
