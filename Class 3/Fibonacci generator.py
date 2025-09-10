from typing import Iterator


def fibonacci_generator() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    gen = fibonacci_generator()
    for _ in range(10):
        print(next(gen))
