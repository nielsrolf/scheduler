from scheduler import Schedule


Schedule().every(3).do(
    lambda i, d: print('Fizz', end='')
).every(5).do(
    lambda i, d: print("Buzz", end='')
).every(1).do(
    lambda i, d: print(i + 1, end='') if ((i + 1) % 3) * ((i + 1) % 5) != 0 else None
).every(1).do(
    lambda i, d: print()
).forNext(100).execute()
