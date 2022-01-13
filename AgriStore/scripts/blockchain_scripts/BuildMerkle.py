from blockchain_scripts.merkle_tree import *


class BuildMerkle:
    def __init__(self, data):
        self.data = data
        self.merkle_tree = self.build_merkle()

    def build_merkle(self):
        """Check for datatype and build merkletree
        :return:
        """
        if type(self.data) == dict:
            return self.dicthash()
        elif type(self.data) == list:
            return self.listhash()
        else:
            raise Exception("data type is not supported, please use dictionary or list")

    def dicthash(self):
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

    def listhash(self):
        mt = MerkleTools(hash_type="sha256")
        mt.add_leaf(self.data, True)
        mt.make_tree()
        return mt
