# https://www.youtube.com/watch?v=alNU9AVWkQk&t=784s
import hashlib
from merkle_tree import MerkleTools

class Block():
    def __init__(self, data, previous_hash):
        self.data = data
        self.hash = hashlib.sha256()
        self.previous_hash = previous_hash
        self.nonce = 0 # the difficulty for mining the block

    def create_hash(self, difficulty):
        # self refers to the class block, if we make a string out of the block class it calls the def __str__ function
        self.hash.update(str(self).encode("utf-8")) # so encode the block
        while int(self.hash.hexdigest(), 16) > 2**(256-difficulty):
            self.nonce += 1
            # reseting this, otherwise using the nonce wont give the same hash
            # since python cumulate nonce times to get the hash without the reset
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode("utf-8"))

    def __str__(self):
        return f"{self.data} {self.previous_hash.hexdigest()} {self.nonce}"

class Chain():
    def __init__(self, difficulty):
        self.difficulty = difficulty
        # all mined blocks
        self.blocks = []
        # all info that get into the block
        self.pool = []
        self.create_first_block()

    def proof_of_work(self, block):
        """
        :param block:
        :return:
        """
        hash = hashlib.sha256()
        hash.update(str(block).encode("utf-8"))
        # check the if the hash and the difficulty is the same and
        # check if the previous hash is correct in line
        return block.block_hash.hexdigest() == hash.hexdigest() and \
               int(hash.hexdigest(), 16) < 2 ** (256-self.difficulty) and \
               block.previous_hash == self.blocks[-1].block_hash

    def add_to_chain(self, block):
        if self.proof_of_work(block):
            self.blocks.append(block)

    def add_to_pool(self, data):
        self.pool.append(data)

    def create_first_block(self):
        hash = hashlib.sha256()
        hash.update(''.encode("utf-8"))
        origin = Block("Origin", hash)
        origin.create_hash(self.difficulty)
        self.blocks.append(origin)

    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data, self.blocks[-1].block_hash)
            block.create_hash(self.difficulty)
            self.add_to_chain(block)
            print("==================================================\n"
                  f"Hash: {block.hash.hexdigest()}\n"
                  f"Previous Hash: {block.previous_hash.hexdigest()}\n"
                  f"Nonce: {block.nonce}\n"
                  f"Data: {block.data}\n"
                  "==================================================")


if __name__ == "__main__":
    chain = Chain(20)
    while(True):
        data = input("Add something to chain:")
        chain.add_to_pool(data)
        chain.mine()



