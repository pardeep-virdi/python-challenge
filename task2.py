

def sum_to_n(number):
    total = 0 
    for num in range(1, number + 1):
          total += num
    return total

if __name__ == "__main__":
    number = 50
    result = sum_to_n(number)
    print("The sum of numbers from 1 to 50 is:", result)
    
