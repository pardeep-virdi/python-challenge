#factorial

def fact(number):
    if number == 0:
        return 1  # Factorial of 0 is 1
    total = 1
    for num in range(1, number + 1):
          total *= num
    return total

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    if number < 0:
       print( number, "is Negative")
       exit()
    result = fact(number)
    print("Factorial of", number, "is:", result )
    
