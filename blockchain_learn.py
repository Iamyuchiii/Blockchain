# https://www.youtube.com/watch?v=MyXndVDCIY8&list=PLTAIl4ewbGt8EuEPqNzMS58MrnUuwNd67&index=11&t=77s
from hashlib import sha256
import json
from datetime import datetime
from merkle_tree import MerkleTools
from tools import *
from copy import deepcopy

# TODO -----------------------------------------------------------------------
# smart contract
# - performs certain actions after meeting the requirement
# certificate TLS / SSL = time limit - refresh token
# - optional for servers
# add fucntion where the info is added after being valid
# make diffuclty -> adjusted by a protocal
# merkle tree -> handle images / make it independent from blockchain
# make one demo where everything should work
# TODO -----------------------------------------------------------------------

class Block:
    def __init__(self, index, previous_hash, merkle_tree, timestamp, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.nonce = 0
        self.difficulty = difficulty
        self.merkle_tree = merkle_tree
        self.merkle_root = self.merkle_tree.get_merkle_root()
        self.block_hash = self.compute_hash()

    def __str__(self):
        """
        :return: when print the block object will be printed in dictionary
        """
        return str(self.__dict__)

    def hashing(self):
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
        print(modification)
        block_string = json.dumps(modification, sort_keys=True)
        print(block_string)
        first_hash = sha256(block_string.encode()).hexdigest()
        second_hash = sha256(first_hash.encode()).hexdigest()
        return second_hash

    def compute_hash(self):
        hash = self.hashing()
        while int(hash, 16) > (2 ** (256 - self.difficulty)):
            self.nonce += 1
            # reseting this, otherwise using the nonce wont give the same hash
            # since python cumulate nonce times to get the hash without the reset
            hash = self.hashing()
        # while not hash.startswith("0" * difficulty):
        #     self.nonce += 1
        #     hash = self.hashing()
        return hash


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
                             "datetime.now().timestap()", 5)
        # add block to the chain
        self.chain.append(origin_block.block_hash)
        # saves the information of the firstblock as dictionary
        self.blocks.append(origin_block.__dict__)

    def getlasthash(self):
        """
        :return: last hashvalue of the blockchain
        """
        return self.chain[-1]

    def getlastblock(self):
        return self.blocks[-1]

    def proof_of_work(self, block):
        """
        Makes a hashvalue according to the difficulty rate
        :param block: a block object
        :return: the hash value met by the difficulty
        """
        # to exclude the current hash to recreate block hash
        modification = without_keys(block.__dict__, {"merkle_tree", "block_hash"})
        block_string = json.dumps(modification, sort_keys=True)
        first_hash = sha256(block_string.encode()).hexdigest()
        second_hash = sha256(first_hash.encode()).hexdigest()
        return second_hash == block.block_hash and \
               self.getlasthash() == block.previous_hash and \
               int(second_hash, 16) < 2 ** (256 - block.difficulty)

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
                      "datetime.now().isoformat()", 5)
        if self.proof_of_work(block):
            # add block to the chain
            self.chain.append(block.block_hash)
            # saves the information of the firstblock as dictionary
            self.blocks.append(block.__dict__)
        else:
            print("aa")
        return self.blocks[-1]


if __name__ == "__main__":
    data = {
        "input" : "asdasdasd",
        "output" : "assdasdasdasd"
    }

    chain = Blockchain()
    chain.add_info(data)
    print(chain.blocks)




# use merkle tree
# one hash for original image
# seconde hash for results
