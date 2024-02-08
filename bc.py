from hashlib import sha256
import json
from time import time
from typing import List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, data: List[List[int]], nonce: int = 0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{json.dumps(self.data)}{self.nonce}"
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        return Block(0, "0", time(), [[]])

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, new_block: Block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

def multiply_matrices(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

# Initialize blockchain
blockchain = Blockchain()

# Example matrices for multiplication
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

# Create a block for matrix multiplication
latest_block = blockchain.get_latest_block()
index = latest_block.index + 1
timestamp = time()
data = multiply_matrices(matrix_a, matrix_b)
new_block = Block(index, latest_block.hash, timestamp, data)

# Add the block to the blockchain
blockchain.add_block(new_block)

# Print the blockchain
for block in blockchain.chain:
    print(f"Block #{block.index}, Hash: {block.hash}, Data: {block.data}")
