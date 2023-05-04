def fibonacci_nums(x):

    fibonacci_list =[0]
    a = 0
    b = 1
    

    while b<=x:
        fibonacci_list.append(b)
        #a becomes b and b becomes a+b as the loop runs
        a,b = b, a+b
    return fibonacci_list
print(f"Find Fibonacci numbers between 0 and x")
x = int(input("Number (x):"))
fib_seq = fibonacci_nums(x)
print(f"Fibonacci numbers between 0 and {x} are: {fib_seq}")

# if __name__ == "__main__":
#     fibonacci_nums(x)
    