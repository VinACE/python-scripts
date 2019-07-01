def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    if n < 2: # base case
        return n
    # breakpoint()
    return fib2(n - 2) + fib2(n - 1)
    # recursive case

if __name__ == "__main__":
    print(fib2(5))