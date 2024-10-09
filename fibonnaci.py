#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

def generate_fibonacci(limit):
    """
    Generate Fibonacci numbers less than the given limit.
    """
    fibonacci_sequence = []
    a, b = 0, 1
    while a < limit:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

def write_to_file(filename, data):
    """
    Write the Fibonacci sequence to a file.
    Handles potential I/O errors.
    """
    try:
        with open(filename, 'w') as file:
            for number in data:
                file.write(f"{number}\n")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

if __name__ == "__main__":
    # Argument parsing for limit and output file name
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers less than a limit and write them to a file.")
    parser.add_argument("limit", type=int, help="The upper limit for Fibonacci numbers.")
    parser.add_argument("output_file", type=str, help="The output file to write Fibonacci numbers.")
    
    args = parser.parse_args()

    # Generate Fibonacci numbers less than the specified limit
    fibonacci_numbers = generate_fibonacci(args.limit)

    # Write Fibonacci numbers to the specified file
    write_to_file(args.output_file, fibonacci_numbers)