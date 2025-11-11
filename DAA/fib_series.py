import time

def fibonacci_iter(n):
    """Iterative Fibonacci with step counting and series generation"""
    if n < 0:
        return None, None, 0  # invalid input case

    if n == 0:
        return [0], 0, 1
    if n == 1:
        return [0, 1], 1, 1

    steps = 0
    a, b = 0, 1
    series = [0, 1]

    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
        series.append(c)
        steps += 1

    return series, series[-1], steps + 1


def fibonacci_recur_helper(n, steps):
    """Recursive helper to compute Fibonacci value with step tracking"""
    steps[0] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recur_helper(n - 1, steps) + fibonacci_recur_helper(n - 2, steps)


def fibonacci_recur_series(n):
    """Generate Fibonacci series using recursion with step tracking"""
    if n < 0:
        return None, None, 0  # invalid input case

    series = []
    total_steps = 0

    for i in range(n + 1):
        steps = [0]
        val = fibonacci_recur_helper(i, steps)
        series.append(val)
        total_steps += steps[0]

    return series, series[-1], total_steps


# Main section
if __name__ == '__main__':
    n = int(input("Enter the number of terms: "))

    if n < 0:
        print("\n⚠️ Invalid Input: Please enter a non-negative number.")
    else:
        # Iterative Fibonacci
        print("\n--- Iterative Fibonacci ---")
        start_time = time.time()
        iter_series, iter_result, iter_steps = fibonacci_iter(n)
        end_time = time.time()
        iter_time = end_time - start_time

        print(f"Series: {iter_series}")
        print(f"nth Fibonacci number: {iter_result}")
        print(f"Steps taken: {iter_steps}")
        print(f"Execution Time: {iter_time:.6f} seconds")

        # Recursive Fibonacci
        print("\n--- Recursive Fibonacci ---")
        start_time = time.time()
        recur_series, recur_result, recur_steps = fibonacci_recur_series(n)
        end_time = time.time()
        recur_time = end_time - start_time

        print(f"Series: {recur_series}")
        print(f"nth Fibonacci number: {recur_result}")
        print(f"Steps taken: {recur_steps}")
        print(f"Execution Time: {recur_time:.6f} seconds")

        # # Complexity Analysis
        # print("\n--- Time and Space Complexity ---")
        # print("Iterative: Time = O(n), Space = O(1)")
        # print("Recursive: Time = O(2^n), Space = O(n)")
