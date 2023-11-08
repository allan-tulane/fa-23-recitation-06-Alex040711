def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    # Base cases: F0 = 0 and F1 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: Fn = Fn-1 + Fn-2
        return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

    
def fib_top_down(n, fibs):
    # Base case: if fibs[n] has been computed, return it
    if fibs[n] != -1:
        return fibs[n]
    # Base cases: F0 = 0 and F1 = 1
    if n == 0:
        fibs[n] = 0
        return 0
    elif n == 1:
        fibs[n] = 1
        return 1
    else:
        # Recursive case: compute Fn, store it in fibs[n], and return it
        fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
        return fibs[n]


def fib_bottom_up(n):
    # If n is 0 or 1, return n (since F0 = 0, F1 = 1)
    if n <= 1:
        return n

    # Initialize a list of n+1 elements to store the Fibonacci sequence
    fibs = [0] * (n + 1)
    fibs[1] = 1  # F1 = 1

    # Iterate from 2 to n, filling in the Fibonacci sequence in the list
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]

    # Return the nth Fibonacci number
    return fibs[n]




def fib_bottom_up_better(n):
    ###TODO
    pass
