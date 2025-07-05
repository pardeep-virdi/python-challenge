def add(a,b):
    print ("Addition:", a + b)

def sub(a,b):
    print ("Subtraction:", a - b)

def mux(a,b):
    print ("Multiplication:", a * b)

def div(a,b):
    print ("Division:", a / b)

if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print ("\n")

    add(a,b)
    sub(a, b)
    mux(a, b)
    div(a, b)
