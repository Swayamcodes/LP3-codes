import heapq
import time

# Node class for Huffman Tree
class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq


# Function to build Huffman Tree using Greedy approach
def build_huffman_tree(freq_map):
    pq = []

    # Step 1: Add all characters to min-heap → O(n log n)
    for ch, freq in freq_map.items():
        heapq.heappush(pq, Node(ch, freq))

    # Step 2: Combine two smallest nodes repeatedly → O(n log n)
    while len(pq) > 1:
        left = heapq.heappop(pq)   # O(log n)
        right = heapq.heappop(pq)  # O(log n)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(pq, parent)  # O(log n)

    # Return root of Huffman Tree
    return pq[0]


# Function to generate Huffman Codes using DFS
def generate_codes(root, code, huffman_codes):
    if root is None:
        return

    # Leaf node: store the code
    if root.left is None and root.right is None:
        huffman_codes[root.ch] = code
        return

    # Recursive traversal
    generate_codes(root.left, code + "0", huffman_codes)
    generate_codes(root.right, code + "1", huffman_codes)


# Encode the input text using Huffman codes
def encode(text, huffman_codes):
    encoded_text = ""
    for ch in text:
        encoded_text += huffman_codes[ch]  # O(1)
    return encoded_text


# Main program
if __name__ == "__main__":
    text = input("Enter text to encode: ")

    print("\n=== HUFFMAN ENCODING ===\n")
    print(f"Original Text: {text}")
    print(f"Length: {len(text)} characters\n")

    # Step 1: Calculate frequency → O(n)
    freq_map = {}
    for ch in text:
        freq_map[ch] = freq_map.get(ch, 0) + 1

    # Step 2: Display frequencies → O(n)
    print("Character Frequencies:")
    for ch, freq in freq_map.items():
        print(f"'{ch}': {freq}")

    start_time = time.time()

    # Step 3: Build Huffman Tree → O(n log n)
    root = build_huffman_tree(freq_map)

    # Step 4: Generate Huffman Codes → O(n)
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)

    # Step 5: Display Huffman Codes → O(n)
    print("\nHuffman Codes:")
    for ch, code in huffman_codes.items():
        print(f"'{ch}': {code}")

    # Step 6: Encode text → O(n)
    encoded_text = encode(text, huffman_codes)
    end_time = time.time()

    print("\nEncoded Text:", encoded_text)
    print(f"Encoded Length: {len(encoded_text)} bits")

    compression_ratio = (len(text) * 8.0) / len(encoded_text)
    print(f"Compression Ratio: {compression_ratio:.2f}")

    print(f"Time Taken: {(end_time - start_time) * 1e6:.2f} µs")

    print("\n=== COMPLEXITY ANALYSIS ===")
    print("Time Complexity: O(n log n)")
    print("  - Frequency calculation: O(n)")
    print("  - Tree construction: O(n log n)")
    print("  - Code generation: O(n)")
    print("  - Encoding: O(n)")
    print("Space Complexity: O(n)")
    print("  - Tree nodes: O(n)")
    print("  - Huffman codes map: O(n)")

"""
--------------------------------------------
DETAILED LOOP-LEVEL TIME COMPLEXITY:
1. Frequency calculation loop → O(n)
2. Min-heap insertion loop → O(n log n)
3. Tree-building loop → O(n log n)
4. Huffman code generation (recursive) → O(n)
5. Encoding loop → O(n)
6. Printing loops → O(n)

TOTAL TIME COMPLEXITY → O(n log n)
TOTAL SPACE COMPLEXITY → O(n)

GREEDY STRATEGY:
-----------------
- Always combine two smallest-frequency nodes.
- Ensures shortest possible average code length.
- Provides optimal prefix-free compression.
--------------------------------------------
"""
