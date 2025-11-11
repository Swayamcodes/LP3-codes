def knapsack_dp(W, wt, val, n):
    """Dynamic Programming solution for 0-1 Knapsack problem.
    Returns maximum profit, selected items, and the DP table."""

    # DP table initialization (n+1) x (W+1)
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Backtrack to find selected items
    selected_items = []
    res = K[n][W]
    w = W

    for i in range(n, 0, -1):
        if res <= 0:
            break
        # Item was not included
        if res == K[i - 1][w]:
            continue
        else:
            # Item included
            selected_items.append(i)
            res -= val[i - 1]
            w -= wt[i - 1]

    selected_items.reverse()
    return K[n][W], selected_items, K


# ---------------- USER INPUT SECTION ----------------
n = int(input("Enter number of items: "))

val = []
wt = []

print("\nEnter weight and value for each item:")
for i in range(n):
    w, v = map(int, input(f"Item {i + 1} (weight value): ").split())
    wt.append(w)
    val.append(v)

W = int(input("\nEnter total capacity of the knapsack: "))

# Function call
max_profit, selected, table = knapsack_dp(W, wt, val, n)

# --------------- OUTPUT SECTION ----------------
print("\n Maximum possible profit =", max_profit)
print(" Items selected:")

if selected:
    for i in selected:
        print(f"  → Item {i}: weight = {wt[i - 1]}, value = {val[i - 1]}")
else:
    print("  No items selected.")

# ---------------- DP TABLE DISPLAY ----------------
print("\n DP Table (Rows = Items, Columns = Capacity):\n")

# Header row
print("     ", end="")
for w in range(W + 1):
    print(f"{w:4}", end="")
print("\n" + "-" * (6 + 5 * (W + 1)))

# Table rows
for i in range(n + 1):
    print(f"i={i:2} |", end="")
    for w in range(W + 1):
        print(f"{table[i][w]:4}", end="")
    print()