def factorial_recursion(n):
    if n == 1:
        return 1
    return n * factorial_recursion(n-1)
        

def factorial_iterative(n):
    answer = 1
    while n > 1:
        answer = answer*n 
        n = n - 1
    return answer


# print (factorial_iterative(5))
# print (factorial_recursion(3))

# 0 ,1 , 1, 2, 3, 5, 8, 13, 21

def fibonacci_recur(n):
    if n < 2:
        return n 
    
    return fibonacci_recur(n-1) + fibonacci_recur(n-2)

def fibonacci_iter(n):
    if n == 1 or n == 2:
        return 1
    first = 0 
    second = 1
    i = 1
    result = 0
    while i < n:
        result = first+second
        first = second
        second = result
        i += 1
    return result

# print(fibonacci_iter(1))
# print(fibonacci_recur(1))




        



