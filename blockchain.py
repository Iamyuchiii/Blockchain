# https://www.youtube.com/watch?v=MyXndVDCIY8&list=PLTAIl4ewbGt8EuEPqNzMS58MrnUuwNd67&index=11&t=77s
from hashlib import sha256
import json
from time import time
from merkle_tree import MerkleTools
from tools import *

# TODO -----------------------------------------------------------------------
# smart contract
# - performs certain actions after meeting the requirement
# certificate TLS / SSL = time limit - refresh token
# - optional for servers
# add fucntion where the info is added after being valid
# make diffuclty -> adjusted by a protocal (hard)
# merkle tree -> handle images / make it independent from blockchain X
# make one demo where everything should work
# TODO -----------------------------------------------------------------------

class Block:
    def __init__(self, index, previous_hash, merkle_tree, timestamp):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.nonce = 0
        self.merkle_tree = merkle_tree
        self.merkle_root = self.merkle_tree.get_merkle_root()
        self.block_hash = self.hash_difficulty()

    def __str__(self):
        """
        :return: when print the block object will be printed in dictionary
        """
        return str(self.__dict__)

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

    def hash_difficulty(self):
        difficulty = 10
        hash = self.compute_hash()
        while int(hash, 16) > (2 ** (256 - difficulty)):
            self.nonce += 1
            # reseting this, otherwise using the nonce wont give the same hash
            # since python cumulate nonce times to get the hash without the reset
            hash = self.compute_hash()
        # while not hash.startswith("0" * difficulty):
        #     self.nonce += 1
        #     hash = self.compute_hash()
        return hash


class Blockchain():
    def __init__(self):
        self.difficulty = 2
        self.blocks = []
        self.genesis_block()

    def __str__(self):
        """
        :return: when print the object the dictonary will be printed
        """
        return str(self.__dict__)

    def genesis_block(self):
        """
        :return: adds a origin dummy block to the blockchain
        """
        mt = BuildMerkle({"user_input" : "dummy"}).merkle_tree
        # makes first block for as dummy data
        genesis = Block("Origin", 0x0, mt,
                             time())
        # saves the information of the firstblock as dictionary
        self.blocks.append(genesis.__dict__)

    def adjust_difficulty(self, block_index):
        if block_index % 2 == 0:
            pass

    def getlastblock(self):
        return self.blocks[-1] if self.blocks else None

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
               self.blocks[-1]["block_hash"] == block.previous_hash and \
               int(second_hash, 16) < 2 ** (256 - 5)

    def add_info(self, mt):
        """
        adds a block with info to the blockchain
        :param data: data in dictionary format
        :return: last block
        """
        block = Block(len(self.blocks), self.blocks[-1]["block_hash"], mt,
                      time())
        if self.proof_of_work(block):
            # saves the information of the firstblock as dictionary
            self.blocks.append(block.__dict__)
            self.adjust_difficulty(len(self.blocks)-1)
        else:
            print("Block is not added to the chain ")

class BuildMerkle():
    def __init__(self, data):
        self.data = data
        self.merkle_tree = self.build_merkle()

    def build_merkle(self):
        if type(self.data) == dict:
            return self.mt_selfthash()
        else:
            raise Exception("data type is not supported, please use "
                            "dictionary")

    def mt_selfthash(self):
        """
        Makes a merkle tree formation using provided data (block_content)
        :param data: block_content from the block
        :return: merkle tree class
        """
        temp = []
        for key, value in self.data.items():
            temp.append(str({key: value}))
        mt = MerkleTools(hash_type="sha256")
        mt.add_leaf(temp, True)
        mt.make_tree()
        return mt

# if __name__ == "__main__":
#     # image data
#     laptop = "D:\master_thesis\Blockchain"
#     computer = r"D:\Blockchain\test_data\test"
#     # string data
#     data = {
#         "input" : "asdasdasd",
#         "output" : "assdasdasdasd"
#     }
#     # processing data
#     processing = Data_processing(computer, type="image")
#     image_hashlist = processing.data_type()
#     # building merkletree
#     mt = BuildMerkle(image_hashlist).merkle_tree
#     mt2 = BuildMerkle(data).merkle_tree
#     # # adding blocks
#     chain = Blockchain()
#     chain.add_info(mt)
#     chain.add_info(mt2)
#     for i in chain.blocks:
#         print(i)





# use merkle tree
# one hash for original image
# seconde hash for results