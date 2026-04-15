# Adaptive-Huffman-Coding
This implementation offers the flexible Huffman coding system which processes data through its selective adaptive coding system.
# Selective Adaptive Huffman Coding Simulator

An interactive, console-based Python implementation of a **Selective Adaptive Huffman Encoder**. This project demonstrates how introducing a threshold (*T*) for tree-updates can drastically reduce computational overhead compared to Traditional Adaptive Huffman coding (like Vitter's algorithm).

## How It Works: The T-Threshold

Traditional adaptive Huffman coding updates its internal binary tree after *every single character* processed. This guarantees optimal compression but demands significant CPU cycles for constant tree rebalancing.

This **Selective** approach introduces a greedy decision rule:
1. It tracks "uncommitted" character frequencies locally.
2. Only when a character's local frequency reaches the **Threshold (*T*)** does the algorithm commit those occurrences to the main tree and trigger a rebuild.
3. Characters that haven't reached the threshold are encoded using the current (slightly outdated) tree or sent as raw "Not Yet Transmitted" (NYT) blocks.

**The Trade-off:** Vastly improved execution speed (fewer tree rebuilds) at the cost of a tiny fraction of compression optimality.

## Getting Started

### Prerequisites
- Python 3.6 or higher.
- No external libraries required (uses standard `heapq`).

### Running the Simulator
1. Save the provided Python code as `huffman.py`.
2. Open your terminal or command prompt.
3. Run the script:
   ```bash
   python huffman.py
   ```
4. Follow the on-screen prompts to enter your data stream and desired threshold.

## Example Usage

```text
==================================================
  Selective Adaptive Huffman Encoder
==================================================

Enter the text you want to encode:
> abracadabra_macadamia

Enter the threshold value (e.g., 3, 5, 10):
> 3

Encoding with Threshold (T) = 3...

==================================================
  RESULTS
==================================================
Original String Length : 21 characters
Total Tree Rebuilds    : 4

Encoded Output:
[a][b][r]0[c]0[d]0[b][r]10[_]11[m]100[c]110[d]100[m]101[i]111

Final Huffman Dictionary:
  'a'    : 0
  'c'    : 100
  'b'    : 101
  'd'    : 110
  'r'    : 1110
  'm'    : 1111
==================================================
```

## 🛠️ Customization
You can easily modify the script to integrate into an actual file-compression pipeline by replacing the simulated string outputs with proper bitwise file-writing (e.g., using Python's `struct` or `bitstring` modules).
