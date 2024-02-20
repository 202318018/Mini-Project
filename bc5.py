import hashlib
import json
import time  # Import the time module to work with timestamps and simulate network delays
import numpy as np
import random

class Blockchain:
    def __init__(self):
        # Initialize the blockchain with an empty list for the chain and pending transactions
        self.chain = []
        self.pending_transactions = []  # Store transactions that have not yet been added to a block
        # Create the genesis block (the first block in the chain) with a predefined previous hash
        self.create_block(previous_hash='1', data='Genesis Block', method='sha256')


    def create_block(self, data, previous_hash, method):
        # Create a new block with given data, the hash of the previous block, and a specified hashing method
        block = {
            'index': len(self.chain) + 1,  # Block number in the chain
            'timestamp': time.time(),  # Current timestamp
            'data': data,  # Data to be stored in the block
            'previous_hash': previous_hash,  # Hash of the previous block to maintain the chain's integrity
        }
        block['hash'] = self.hash(block, method)  # Generate the current block's hash
        self.chain.append(block)  # Add the new block to the chain
        self.send_to_central_server(block)  # Simulate sending the block to a centralized server
        return block

    def hash(self, block, method):
        # Generate a hash of the block based on the specified method (SHA-256 or simulated homomorphic encryption)
        encoded_block = json.dumps(block, sort_keys=True).encode()  # Convert the block into a string and encode it
        if method == 'sha256':
            return hashlib.sha256(encoded_block).hexdigest()  # Use SHA-256 hashing
        elif method == 'he':  # Placeholder for homomorphic encryption
            return "he_" + hashlib.sha256(encoded_block).hexdigest()  # Simulate HE by prefixing SHA-256 hash
        else:
            raise ValueError("Unsupported hashing method")  # Raise an error if an unknown method is specified

    def add_block(self, matrix1, matrix2):
        # Add a block to the chain with the result of multiplying two matrices
        previous_block = self.chain[-1]  # Get the last block in the chain
        result_matrix = np.dot(matrix1, matrix2).tolist()  # Perform matrix multiplication and convert the result to a list
        start_time = time.time()  # Record the start time for adding the block
        method = 'sha256' if (len(self.chain) + 1) % 2 == 0 else 'he'  # Alternate between SHA-256 and HE for demonstration
        block = self.create_block(data=result_matrix, previous_hash=previous_block['hash'], method=method)
        end_time = time.time()  # Record the end time for adding the block
        return block, end_time - start_time  # Return the new block and the time taken to add it

    @staticmethod
    def send_to_central_server(block):
        # Simulate sending a block to a centralized server
        print(f"Sending block {block['index']} to the central server with hash {block['hash'][:6]}...")
        time.sleep(1)  # Simulate a network delay
        print(f"Block {block['index']} received by the central server.")
    
    def validate_chain(self):
        # Validate the integrity of the entire blockchain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]  # Current block being validated
            previous_block = self.chain[i-1]  # Previous block in the chain
            # Check if the previous_hash recorded in the current block matches the hash of the previous block
            if current_block['previous_hash'] != self.hash(previous_block, previous_block.get('method', 'sha256')):
                return f"Chain is altered at block index {i}"  # Report alteration if there's a mismatch
            # Verify the current block's hash is accurate based on its content and method
            if current_block['hash'] != self.hash(current_block, current_block.get('method', 'sha256')):
                return f"Chain is altered at block index {i}"
        return "The chain is valid."  # Return a message indicating the chain is valid if no alterations are found

# Example usage
blockchain = Blockchain()

# Define two 2x2 matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Add blocks with matrix multiplication results
block1, time1 = blockchain.add_block(matrix1, matrix2)
print(f"Block 1 added in {time1} seconds")
print(json.dumps(block1, indent=4, sort_keys=True))

block2, time2 = blockchain.add_block(matrix1, matrix2)
print(f"Block 2 added in {time2} seconds")
print(json.dumps(block2, indent=4, sort_keys=True))

# Validate the blockchain before any tampering
print(blockchain.validate_chain())

# Simulate tampering
blockchain.chain[1]['data'] = "Tampered Data"

# Validate the blockchain after tampering
print(blockchain.validate_chain())