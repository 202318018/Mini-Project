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
    # Genesis block has index 0 and arbitrary previous hash
    return Block(0, "0", time(), {"matrix": None, "result": None}, calculate_hash(0, "0", time(), {"matrix": None, "result": None}))

def create_block(index, previous_hash, data):
    timestamp = time()
    hash_value = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, hash_value)

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

if __name__ == "__main__":
    # Create Genesis Block
    blockchain = [create_genesis_block()]

    # Sample matrices for multiplication
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]

    # Perform matrix multiplication and add result to the blockchain
    result_matrix = matrix_multiply(matrix_a, matrix_b)
    block_data = {"matrix": result_matrix, "result": None}
    new_block = create_block(blockchain[-1].index + 1, blockchain[-1].hash, block_data)
    blockchain.append(new_block)

    # Display the blockchain
    matrix_a2 = [[9, 10], [11, 12]]
    matrix_b2 = [[13, 14], [15, 16]]

    # Perform the second matrix multiplication and add the result to the blockchain
    result_matrix2 = matrix_multiply(matrix_a2, matrix_b2)
    block_data2 = {"matrix": result_matrix2, "result": None}
    new_block2 = create_block(blockchain[-1].index + 1, blockchain[-1].hash, block_data2)
    add_block_to_chain(blockchain, new_block2)

    matrix_a3 = [[12, 10], [11, 2]]
    matrix_b3 = [[13, 4], [15, 16]]

    # Perform the second matrix multiplication and add the result to the blockchain
    result_matrix3 = matrix_multiply(matrix_a3, matrix_b3)
    block_data3 = {"matrix": result_matrix3, "result": None}
    new_block3 = create_block(blockchain[-1].index + 1, blockchain[-1].hash, block_data3)
    add_block_to_chain(blockchain, new_block3)

    matrix_a4 = [[2, 10], [1, 2]]
    matrix_b4 = [[3, 4], [1, 6]]

    # Perform the second matrix multiplication and add the result to the blockchain
    result_matrix4 = matrix_multiply(matrix_a4, matrix_b4)
    block_data4 = {"matrix": result_matrix4, "result": None}
    new_block4 = create_block(blockchain[-1].index + 1, blockchain[-1].hash, block_data4)
    add_block_to_chain(blockchain, new_block4)
    # Display the blockchain after the second multiplication
    display_chain(blockchain)
