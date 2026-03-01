def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using a simple recursive algorithm.

    The sequence is defined as::

        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1

    This implementation has exponential time complexity and is meant
    for educational purposes rather than performance.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # simple demonstration
    import sys

    try:
        arg = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        print("Please provide an integer argument.")
        sys.exit(1)

    print(f"Fibonacci({arg}) = {fibonacci(arg)}")