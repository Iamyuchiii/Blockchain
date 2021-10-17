# https://www.youtube.com/watch?v=MyXndVDCIY8&list=PLTAIl4ewbGt8EuEPqNzMS58MrnUuwNd67&index=11&t=77s
from hashlib import sha256
import json
from datetime import datetime
from merkle_tree import MerkleTools
from tools import *
##############################################################################
import os
from PIL import Image
import imagehash
##############################################################################

# TODO -----------------------------------------------------------------------
# smart contract
# - performs certain actions after meeting the requirement
# certificate TLS / SSL = time limit - refresh token
# - optional for servers
# add fucntion where the info is added after being valid
# make diffuclty -> adjusted by a protocal
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
        difficulty = 5
        hash = self.compute_hash()
        while int(hash, 16) > (2 ** (256 - difficulty)):
            self.nonce += 1
            # reseting this, otherwise using the nonce wont give the same hash
            # since python cumulate nonce times to get the hash without the reset
            hash = self.compute_hash()
        # while not hash.startswith("0" * difficulty):
        #     self.nonce += 1
        #     hash = self.hashing()
        return hash


class Blockchain():
    def __init__(self):
        self.chain = []
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
                             "datetime.now().timestap()")
        # add block to the chain
        self.chain.append(genesis.block_hash)
        # saves the information of the firstblock as dictionary
        self.blocks.append(genesis.__dict__)

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
               int(second_hash, 16) < 2 ** (256 - 5)

    def add_info(self, mt):
        """
        adds a block with info to the blockchain
        :param data: data in dictionary format
        :return: last block
        """
        block = Block(len(self.chain), self.chain[-1], mt,
                      "datetime.now().isoformat()")
        if self.proof_of_work(block):
            # add block to the chain
            self.chain.append(block.block_hash)
            # saves the information of the firstblock as dictionary
            self.blocks.append(block.__dict__)
        else:
            print("aa")
        return self.blocks[-1]

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

class Data_processing():
    def __init__(self, data, type="dictionary"):
        self.data = data
        self.type = type

    def data_type(self):
        if self.type.lower() == "image":
            image_list = self.image_processing()
            return self.image_hasing(image_list)

        elif self.type.lower() == "dictionary":
            return self.data
        else:
            raise Exception("Cant process this type of data")

    def image_processing(self):
        saved_image = []
        base_path = self.data
        for image in os.listdir(base_path):
            image_file = os.path.join(base_path, image)
            try:
                saved_image.append(Image.open(image_file))
            except Exception as error:
                print(f"Error found: {error}")
        return saved_image

    def image_hasing(self, image_list):
        image_hash = {}
        for image in image_list:
            hash = imagehash.average_hash(image)
            filename = image.filename.split("\\")[-1]
            image_hash[filename]=str(hash)
        return image_hash




if __name__ == "__main__":
    # image data
    laptop = "D:\master_thesis\Blockchain"
    computer = r"D:\Blockchain\test_data\test"
    # string data
    data = {
        "input" : "asdasdasd",
        "output" : "assdasdasdasd"
    }

    # processing data
    processing = Data_processing(computer, type="image")
    image_hashlist = processing.data_type()
    # building merkletree
    mt = BuildMerkle(image_hashlist).merkle_tree
    # adding blocks
    chain = Blockchain()
    chain.add_info(mt)
    for i in chain.blocks:
        print(i)
    print(chain.chain)





# use merkle tree
# one hash for original image
# seconde hash for results
