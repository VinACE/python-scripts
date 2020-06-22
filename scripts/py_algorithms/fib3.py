from typing import Dict 
memo : Dict[int, int] = { 0:0, 1:1}

print(f'memo is {memo}')

def fib3(n : int) -> int:
    # breakpoint()
    if n not in memo:
        print(f' n is {n}')
        memo[n] = fib3(n-1) + fib3(n-2)
        print(f' Dict memo is {memo[n]}')
    return memo[n]

if __name__ == "__main__":
    print(f' calling fib n = {fib3(5)} ')