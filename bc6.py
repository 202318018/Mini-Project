import hashlib
import json
from time import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + json.dumps(data, sort_keys=True)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", time(), {"matrix": None, "result": None}, calculate_hash(0, "0", time(), {"matrix": None, "result": None}))

def create_block(index, previous_hash, matrix_a, matrix_b):
    timestamp = time()
    result_matrix = matrix_multiply(matrix_a, matrix_b)
    block_data = {"matrix": result_matrix, "result": None}
    hash_value = calculate_hash(index, previous_hash, timestamp, block_data)
    return Block(index, previous_hash, timestamp, block_data, hash_value)

def matrix_multiply(a, b):
    result = [[sum(i*j for i, j in zip(row, col)) for col in zip(*b)] for row in a]
    return result

def add_block_to_chain(chain, block):
    chain.append(block)

def display_chain(chain):
    for block in chain:
        print("Index:", block.index)
        print("Previous Hash:", block.previous_hash)
        print("Timestamp:", block.timestamp)
        print("Data:", block.data)
        print("Hash:", block.hash)
        print("\n")
def combine_blocks(block1, block2):
    combined_data = {
        "matrix_1": block1.data["matrix"],
        "result_1": block1.data["result"],
        "matrix_2": block2.data["matrix"],
        "result_2": block2.data["result"]
    }

    combined_block = create_block(block2.index + 1, block1.hash, combined_data["matrix_2"], combined_data["matrix_1"])
    return combined_block

if __name__ == "__main__":
    # Create Genesis Block
    blockchain = [create_genesis_block()]

    # Block 1 - Matrix Multiplication
    matrix_a1 = [[1, 2], [3, 4]]
    matrix_b1 = [[5, 6], [7, 8]]
    new_block1 = create_block(blockchain[-1].index + 1, blockchain[-1].hash, matrix_a1, matrix_b1)
    add_block_to_chain(blockchain, new_block1)

    # Block 2 - Matrix Multiplication
    matrix_a2 = [[9, 10], [11, 12]]
    matrix_b2 = [[13, 14], [15, 16]]
    new_block2 = create_block(blockchain[-1].index + 1, blockchain[-1].hash, matrix_a2, matrix_b2)
    add_block_to_chain(blockchain, new_block2)

    # Combine the last two blocks in the blockchain
    combined_block = combine_blocks(blockchain[-2], blockchain[-1])

    # Display the combined block
    print("Combined Block:")
    print("Index:", combined_block.index)
    print("Previous Hash:", combined_block.previous_hash)
    print("Timestamp:", combined_block.timestamp)
    print("Data:", combined_block.data)
    print("Hash:", combined_block.hash)

    # Display the entire blockchain
    display_chain(blockchain)
