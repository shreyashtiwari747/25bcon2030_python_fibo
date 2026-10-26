def fibonacci(n):
    """Return the first n Fibonacci numbers as a list."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    count = int(input("How many Fibonacci numbers? "))
    print(fibonacci(count))
