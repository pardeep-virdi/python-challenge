

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number"
    else:
        return f"{number} is an odd number"

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    result = check_even_odd(number)
    print(result)
    
