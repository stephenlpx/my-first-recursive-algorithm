def get_factorial(n):
    #below are the base cases which is used to terminate the recursive algorithm
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        #if the number does not reach the target, then repeat and store the value until the target is hit
        #then return the final value 
        return n * get_factorial(n - 1)

print(get_factorial(6))