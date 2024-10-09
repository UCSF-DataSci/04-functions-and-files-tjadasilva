#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

import argparse

def generate_fibonacci(limit):
    """
    Generate Fibonacci numbers less than the given limit.
    """
    fibs = []
    a, b = 0, 1
    while a < limit:
        fibs.append(a)
        a, b = b, a + b
    return fibs

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def largest_prime_fibonacci(limit):
    """
    Find the largest prime Fibonacci number less than the given limit.
    """
    fib_numbers = generate_fibonacci(limit)
    prime_fibs = [num for num in fib_numbers if is_prime(num)]
    return max(prime_fibs) if prime_fibs else None

if __name__ == "__main__":
    # Argument parsing for the upper limit
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number less than a limit.")
    parser.add_argument("limit", type=int, help="The upper limit for Fibonacci numbers.")
    
    args = parser.parse_args()

    # Find the largest prime Fibonacci number less than the specified limit
    result = largest_prime_fibonacci(args.limit)

    if result:
        print(f"The largest prime Fibonacci number less than {args.limit} is {result}")
    else:
        print(f"There are no prime Fibonacci numbers less than {args.limit}")

# The largest prime Fibonacci number less than 50000 is 28657.