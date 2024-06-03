#!/usr/bin/env python3

def print_fibonacci(length):
    if length < 1:
        print([])  
        return []

    if length == 1:
        print([0]) 
        return [0]

    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    result = fibonacci_sequence[:length]
    print(result)
    return result

