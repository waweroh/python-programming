def fibonacci_nums(n):
    fibonacci_list =[0]
    a=0
    b=1
    

    while b<=n:
        fibonacci_list.append(b)
        a,b = b, a+b
        return fibonacci_list
    # print ("fib:")
    # n = int(input("Number (n):"))
    fib_seq = fibonacci_nums(100)
    # print (f"fibonacci numbers between 0 and {n} are:{fib_seq}")
    print(fib_seq)
    