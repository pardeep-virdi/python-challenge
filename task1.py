# Task 1: Read a File and Handle Errors

filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        for n, line in enumerate(file, start=1):
            print(f"line{n}: {line}", end='')  # end='' avoids adding extra newlines
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
