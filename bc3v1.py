import hashlib
import json
from time import time
from bc4 import display_chain, matrix_multiply

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash_algorithm, hash_value):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash_algorithm = hash_algorithm
        self.hash_value = hash_value

def calculate_hash(index, previous_hash, timestamp, data, hash_algorithm="sha256"):
    value = str(index) + str(previous_hash) + str(timestamp) + json.dumps(data, sort_keys=True)
    
    if hash_algorithm == "sha256":
        return hashlib.sha256(value.encode()).hexdigest()
    elif hash_algorithm == "sha512":
        return hashlib.sha512(value.encode()).hexdigest()
    elif hash_algorithm == "sha128":
        return hashlib.sha1(value.encode()).hexdigest()
    else:
        raise ValueError("Invalid hash algorithm")

def create_genesis_block():
    hash_algorithm = "sha256"
    hash_value = calculate_hash(0, "0", time(), {"matrix": None, "result": None}, hash_algorithm)
    return Block(0, "0", time(), {"matrix": None, "result": None}, hash_algorithm, hash_value)

def create_block(index, previous_hash, data, hash_algorithm="sha256"):
    timestamp = time()
    hash_value = calculate_hash(index, previous_hash, timestamp, data, hash_algorithm)
    return Block(index, previous_hash, timestamp, data, hash_algorithm, hash_value)
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
        print("Hash Algorithm:", block.hash_algorithm)
        print("Hash Value:", block.hash_value)  # Corrected line
        print("\n")

if __name__ == "__main__":
       blockchain = [create_genesis_block()]

    # Sample matrices for the first multiplication
       matrix_a = [[1, 2], [3, 4]]
       matrix_b = [[5, 6], [7, 8]]

    # Perform the first matrix multiplication and add the result to the blockchain
       result_matrix = matrix_multiply(matrix_a, matrix_b)
       block_data = {"matrix": result_matrix, "result": None}
       new_block1 = create_block(blockchain[-1].index + 1, blockchain[-1].hash_value, block_data, hash_algorithm="sha256")
       add_block_to_chain(blockchain, new_block1)

    # Sample matrices for the second multiplication (different matrices)
       matrix_a2 = [[9, 10], [11, 12]]
       matrix_b2 = [[13, 14], [15, 16]]

    # Perform the second matrix multiplication and add the result to the blockchain
       result_matrix2 = matrix_multiply(matrix_a2, matrix_b2)
       block_data2 = {"matrix": result_matrix2, "result": None}
       new_block2 = create_block(blockchain[-1].index + 1, new_block1.hash_value, block_data2, hash_algorithm="sha512")
       add_block_to_chain(blockchain, new_block2)

    # Sample matrices for the third multiplication
       matrix_a3 = [[12, 10], [11, 2]]
       matrix_b3 = [[13, 4], [15, 16]]

    # Perform the third matrix multiplication and add the result to the blockchain
       result_matrix3 = matrix_multiply(matrix_a3, matrix_b3)
       block_data3 = {"matrix": result_matrix3, "result": None}
       new_block3 = create_block(blockchain[-1].index + 1, new_block2.hash_value, block_data3, hash_algorithm="sha128")
       add_block_to_chain(blockchain, new_block3)

    # Sample matrices for the fourth multiplication
       matrix_a4 = [[2, 10], [1, 2]]
       matrix_b4 = [[3, 4], [1, 6]]

    # Perform the fourth matrix multiplication and add the result to the blockchain
       result_matrix4 = matrix_multiply(matrix_a4, matrix_b4)
       block_data4 = {"matrix": result_matrix4, "result": None}
       new_block4 = create_block(blockchain[-1].index + 1, new_block3.hash_value, block_data4, hash_algorithm="sha256")
       add_block_to_chain(blockchain, new_block4)

    # Display the blockchain after the second multiplication
       display_chain(blockchain)
