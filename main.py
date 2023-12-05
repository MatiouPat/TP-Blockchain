import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_info = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_info.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        previous_hash = previous_block.hash
        new_block = Block(index, timestamp, data, previous_hash)
        self.chain.append(new_block)

# Example usage
my_blockchain = Blockchain()
my_blockchain.add_block("Transaction Data 1")
my_blockchain.add_block("Transaction Data 2")

# Print blockchain
for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("\n")