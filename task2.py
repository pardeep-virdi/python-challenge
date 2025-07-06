# Task 2: Write and Append Data to a File

filename = "output.txt"

# Step 1: Take user input and write to the file
data_to_write = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(data_to_write + "\n")

# Step 2: Append additional data to the same file
data_to_append = input("Enter additional text to append to the file: ")
with open(filename, "a") as file:
    file.write(data_to_append + "\n")

# Step 3: Read and display the final content of the file
print(f"\nFinal content of {filename}:")
with open(filename, "r") as file:
    for line in file:
        print(line, end="")
