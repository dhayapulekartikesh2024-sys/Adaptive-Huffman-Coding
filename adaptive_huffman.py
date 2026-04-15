import heapq

class Node:
    """A standard node for the Huffman Tree."""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define less-than for the priority queue (heap)
    def __lt__(self, other):
        return self.freq < other.freq

class SelectiveAdaptiveHuffman:
    def __init__(self, threshold=5):
        self.threshold = threshold
        
        # active_freqs: The absolute frequencies currently defining the tree
        self.active_freqs = {}
        
        # delta_tracker: Tracks localized occurrences since the last tree update
        self.delta_tracker = {}
        
        # The current dictionary of bit-codes
        self.codes = {}

    def _build_tree_and_codes(self):
        """Rebuilds the Huffman tree using only the committed 'active' frequencies."""
        if not self.active_freqs:
            return

        heap = [Node(char, f) for char, f in self.active_freqs.items()]
        heapq.heapify(heap)

        # Edge case: If there is only one unique character in the tree so far
        if len(heap) == 1:
            self.codes[heap[0].char] = "0"
            return

        # Build the tree
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)

        # Generate the new codes
        self.codes = {}
        self._generate_codes(heap[0], "")

    def _generate_codes(self, node, current_code):
        """Traverses the tree to assign 0s and 1s."""
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = current_code
        self._generate_codes(node.left, current_code + "0")
        self._generate_codes(node.right, current_code + "1")

    def encode(self, data_stream):
        """Encodes the data stream using the selective update rule."""
        encoded_output = []
        tree_updates = 0

        for char in data_stream:
            # 1. Output the code using the CURRENT, potentially "outdated" tree
            if char in self.codes:
                encoded_output.append(self.codes[char])
            else:
                # NYT (Not Yet Transmitted) handling. 
                encoded_output.append(f"[{char}]")

            # 2. Track the delta (uncommitted) frequency locally
            self.delta_tracker[char] = self.delta_tracker.get(char, 0) + 1

            # 3. The Greedy Decision Rule: Check if Δf reaches the Threshold
            if self.delta_tracker[char] >= self.threshold:
                
                # Commit the deltas to the active tree frequencies
                self.active_freqs[char] = self.active_freqs.get(char, 0) + self.delta_tracker[char]
                
                # Reset the delta tracker for this character
                self.delta_tracker[char] = 0 

                # Rebuild the tree with the new committed weights
                self._build_tree_and_codes()
                tree_updates += 1

        return "".join(encoded_output), tree_updates

# ==========================================
# Interactive Execution
# ==========================================
if __name__ == "__main__":
    print("=" * 50)
    print("  Selective Adaptive Huffman Encoder")
    print("=" * 50)
    
    # 1. Take User Input for the Data
    data = input("\nEnter the text you want to encode:\n> ")
    
    # Check for empty input
    if not data.strip():
        print("Error: You must enter some text to encode.")
        exit()

    # 2. Take User Input for the Threshold
    while True:
        try:
            threshold_input = input("\nEnter the threshold value (e.g., 3, 5, 10):\n> ")
            threshold_value = int(threshold_input)
            if threshold_value > 0:
                break
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # 3. Run the Encoder
    print(f"\nEncoding with Threshold (T) = {threshold_value}...")
    encoder = SelectiveAdaptiveHuffman(threshold=threshold_value)
    encoded_string, updates = encoder.encode(data)
    
    # 4. Print the Results
    print("\n" + "=" * 50)
    print("  RESULTS")
    print("=" * 50)
    print(f"Original String Length : {len(data)} characters")
    print(f"Total Tree Rebuilds    : {updates}")
    print(f"\nEncoded Output:\n{encoded_string}")
    
    print("\nFinal Huffman Dictionary:")
    for char, code in sorted(encoder.codes.items(), key=lambda x: len(x[1])):
        # Format the output so spaces/newlines are clearly visible
        display_char = repr(char) if char.isspace() else f"'{char}'"
        print(f"  {display_char:<6} : {code}")
    print("=" * 50)
