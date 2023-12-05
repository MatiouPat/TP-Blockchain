import time

from block import Block


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