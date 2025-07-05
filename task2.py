#greeting.py

def greeting(first_name, last_name):
    print("Hello,", first_name, last_name + "!","Welcome to the Python program." )

if __name__ == "__main__":

    first_name = input("Enter the firstname: ")
    last_name = input("Enter the lastname: ")
    print ("\n")
    greeting(first_name, last_name)
