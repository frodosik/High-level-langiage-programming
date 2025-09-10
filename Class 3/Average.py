from typing import List


def average(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    sample_numbers = [1.0, 2.5, 3.75, 4.0]
    print(f"Średnia: {average(sample_numbers)}")
