import math

def sum_of_digits(number : int)->None:
    str_number = str(number)
    sum = 0
    for digit in str_number:
        sum+=int(digit)

    return sum

n = 100

n_factorial = math.factorial(100)
sum = sum_of_digits(n_factorial)
print(f"sum of digits in a {n}: {sum}")

