# Prime numbers
- The code imports the math module, which provides mathematical functions and operations.

- The num_prime(num) function takes a number num as input and returns True if the number is prime and False otherwise.

- Inside the num_prime(num) function:

- If num is less than 2, which is the smallest prime number, the function immediately returns False.
- The function then iterates through each digit in the range from 2 to the square root of num (inclusive) using the range() function and math.sqrt() function.
- The code then uses a for loop to iterate through each digit in the range from 2 to 1000 using the range() function.

- Inside the loop, it calls the num_prime(digit) function to check if the current digit is prime.

- If num_prime(digit) returns True, indicating that the digit is prime, it prints the digit.