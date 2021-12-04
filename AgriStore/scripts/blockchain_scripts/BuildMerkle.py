from merkle_tree import *


class BuildMerkle:
    def __init__(self, data):
        self.data = data
        self.merkle_tree = self.build_merkle()

    def build_merkle(self):
        if type(self.data) == dict:
            return self.mt_selfthash()
        else:
            raise Exception("data type is not supported, please use " "dictionary")

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