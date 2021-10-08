# https://www.youtube.com/watch?v=MyXndVDCIY8&list=PLTAIl4ewbGt8EuEPqNzMS58MrnUuwNd67&index=11&t=77s
from hashlib import sha256
import json
from datetime import datetime
from merkle_tree import MerkleTools
from tools import *

# smart contract
# certificate TLS / SSL = time limit - refresh token

class Block:
    def __init__(self, index, previous_hash, merkle_tree, timestamp, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.nonce = nonce
        self.merkle_tree = merkle_tree
        self.merkle_root = self.merkle_tree.get_merkle_root()
        self.block_hash = self.compute_hash()

    def compute_hash(self):
        """
        Makes double hash from the information store in the block in form of
        dictionary
        :return: double hashed hashcode from the information obtained from the
        block
        """
        # self.__dict__ makes dictionary from the self.variables
        # modification removes merkle_tree class from the dictionary in order
        # to make hashing work
        modification = without_keys(self.__dict__, {"merkle_tree"})
        block_string = json.dumps(modification, sort_keys=True)
        first_hash = sha256(block_string.encode()).hexdigest()
        second_hash = sha256(first_hash.encode()).hexdigest()
        return second_hash


    def __str__(self):
        """
        :return: when print the block object will be printed in dictionary
        """
        return str(self.__dict__)

class Blockchain():
    def __init__(self):
        self.chain = []
        self.blocks = []
        self.origin_block()

    def __str__(self):
        """
        :return: when print the object the dictonary will be printed
        """
        return str(self.__dict__)

    def origin_block(self):
        """
        :return: adds a origin dummy block to the blockchain
        """
        mt = self.build_merkle_tree({"user_input" : "dummy"})
        # makes first block for as dummy data
        origin_block = Block("Origin", 0x0, mt,
                             "datetime.now().timestap()",0)
        origin_block.block_hash = origin_block.compute_hash()
        # add block to the chain
        self.chain.append(origin_block.block_hash)
        # saves the information of the firstblock as dictionary
        self.blocks.append(str(origin_block.__dict__))

    def getlastblock(self):
        """
        :return: last hashvalue of the blockchain
        """
        return self.chain[-1]

    def proof_of_work(self, block):
        """
        Makes a hashvalue according to the difficulty rate
        :param block: a block object
        :return: the hash value met by the difficulty
        """
        difficulty = 5
        block.nonce = 0
        hash = block.compute_hash()
        while int(hash, 16) > (2 ** (256 - difficulty)):
            block.nonce += 1
            # reseting this, otherwise using the nonce wont give the same hash
            # since python cumulate nonce times to get the hash without the reset
            hash = block.compute_hash()
        return hash
        # while not hash.startswith("0" * difficulty):
        #     block.nonce += 1
        #     hash = block.compute_hash()
        # return hash
        # No diffculty requirement each step

    def build_merkle_tree(self, data):
        """
        Makes a merkle tree formation using provided data (block_content)
        :param data: block_content from the block
        :return: merkle tree class
        """
        temp = []
        for key, value in data.items():
            temp.append(str({key: value}))
        mt = MerkleTools(hash_type="sha256")
        mt.add_leaf(temp, True)
        mt.make_tree()
        return mt

    def add_info(self, data):
        """
        adds a block with info to the blockchain
        :param data: data in dictionary format
        :return: last block
        """
        mt = self.build_merkle_tree(data)
        block = Block(len(self.chain), self.chain[-1], mt,
                      datetime.now().timestamp(), 0)
        block.block_hash = self.proof_of_work(block)
        # add block to the chain
        self.chain.append(block.block_hash)
        # saves the information of the firstblock as dictionary
        self.blocks.append(block.__dict__)
        return self.blocks[-1]


if __name__ == "__main__":
    data = {
        "input" : "asdasdasd",
        "output" : "assdasdasdasd"
    }

    chain = Blockchain()
    chain.add_info(data)
    for i in chain.blocks:
        print(i)


# use merkle tree
# one hash for original image
# seconde hash for results
