from blockChain import Blockchain

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