# class MerkleTreeNode:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value
#         self.hashValue = hashlib.sha256(value.encode('utf-8')).hexdigest()
#
#
# def buildTree(leaves):
#     nodes = []
#     for i in leaves:
#         nodes.append(MerkleTreeNode(i))
#
#     while len(nodes) != 1:
#         temp = []
#         for i in range(0, len(nodes), 2):
#             node1 = nodes[i]
#             if i + 1 < len(nodes):
#                 node2 = nodes[i + 1]
#             else:
#                 temp.append(nodes[i])
#                 break
#             print(
#                 "Left child : " + node1.value + " | Hash : " + node1.hashValue + " \n")
#             print(
#                 "Right child : " + node2.value + " | Hash : " + node2.hashValue + " \n")
#             concatenatedHash = node1.hashValue + node2.hashValue
#             parent = MerkleTreeNode(concatenatedHash)
#             parent.left = node1
#             parent.right = node2
#             print(
#                 "Parent(concatenation of " + node1.value + " and " + node2.value + ") : " + parent.value + " | Hash : " + parent.hashValue + " \n")
#             temp.append(parent)
#         nodes = temp
#     return nodes[0]


import hashlib
import binascii
import sys


if sys.version_info < (3, 6):
    try:
        import sha3
    except:
        from warnings import warn
        warn("sha3 is not working!")


class MerkleTools(object):
    def __init__(self, hash_type="sha256"):
        hash_type = hash_type.lower()
        if hash_type in ['sha256', 'md5', 'sha224', 'sha384', 'sha512',
                         'sha3_256', 'sha3_224', 'sha3_384', 'sha3_512']:
            self.hash_function = getattr(hashlib, hash_type)
        else:
            raise Exception('`hash_type` {} nor supported'.format(hash_type))

        self.reset_tree()

    def _to_hex(self, x):
        try:  # python3
            return x.hex()
        except:  # python2
            return binascii.hexlify(x)

    def reset_tree(self):
        self.leaves = list()
        self.levels = None
        self.is_ready = False

    def add_leaf(self, values, do_hash=False):
        self.is_ready = False
        # check if single leaf
        if not isinstance(values, tuple) and not isinstance(values, list):
            values = [values]
        for v in values:
            if do_hash:
                v = v.encode('utf-8')
                v = self.hash_function(v).hexdigest()
            v = bytearray.fromhex(v)
            self.leaves.append(v)

    def get_leaf(self, index):
        return self._to_hex(self.leaves[index])

    def get_leaf_count(self):
        return len(self.leaves)

    def get_tree_ready_state(self):
        return self.is_ready

    def _calculate_next_level(self):
        solo_leave = None
        N = len(self.levels[0])  # number of leaves on the level
        if N % 2 == 1:  # if odd number of leaves on the level
            solo_leave = self.levels[0][-1]
            N -= 1

        new_level = []
        for l, r in zip(self.levels[0][0:N:2], self.levels[0][1:N:2]):
            new_level.append(self.hash_function(l+r).digest())
        if solo_leave is not None:
            new_level.append(solo_leave)
        self.levels = [new_level, ] + self.levels  # prepend new level

    def make_tree(self):
        self.is_ready = False
        if self.get_leaf_count() > 0:
            self.levels = [self.leaves, ]
            while len(self.levels[0]) > 1:
                self._calculate_next_level()
        self.is_ready = True

    def get_merkle_root(self):
        if self.is_ready:
            if self.levels is not None:
                return self._to_hex(self.levels[0][0])
            else:
                return None
        else:
            return None

    def get_proof(self, index):
        if self.levels is None:
            return None
        elif not self.is_ready or index > len(self.leaves)-1 or index < 0:
            return None
        else:
            proof = []
            for x in range(len(self.levels) - 1, 0, -1):
                level_len = len(self.levels[x])
                if (index == level_len - 1) and (level_len % 2 == 1):  # skip if this is an odd end node
                    index = int(index / 2.)
                    continue
                is_right_node = index % 2
                sibling_index = index - 1 if is_right_node else index + 1
                sibling_pos = "left" if is_right_node else "right"
                sibling_value = self._to_hex(self.levels[x][sibling_index])
                proof.append({sibling_pos: sibling_value})
                index = int(index / 2.)
            return proof

    def validate_proof(self, proof, target_hash, merkle_root):
        merkle_root = bytearray.fromhex(merkle_root)
        target_hash = bytearray.fromhex(target_hash)
        if len(proof) == 0:
            return target_hash == merkle_root
        else:
            proof_hash = target_hash
            print(proof)
            for p in proof:
                try:
                    # the sibling is a left node
                    sibling = bytearray.fromhex(p['left'])
                    proof_hash = self.hash_function(sibling + proof_hash).digest()
                except:
                    # the sibling is a right node
                    print(p["right"]+"__________________________")
                    sibling = bytearray.fromhex(p['right'])
                    proof_hash = self.hash_function(proof_hash + sibling).digest()

                print(proof_hash)
                print(merkle_root)
            return proof_hash == merkle_root


if __name__ == "__main__":
    mt = MerkleTools()

    mt.add_leaf(["tierion", "hallo123"], True)
    mt.add_leaf(["bitcoin", "blockchain"], True)

    mt.make_tree()

    print("root:", mt.get_merkle_root())
    #
    # print(mt.get_proof(0))
    # print(mt.get_leaf(0))
    # print(mt.get_proof(1))
    # print(mt.get_leaf(1))
    # print(mt.get_proof(2))
    # print(mt.get_leaf(2))
    # print(mt.get_proof(3))
    # print(mt.get_leaf(3))

    # print(mt.validate_proof(mt.get_proof(0), mt.get_leaf(0),
    #                         mt.get_merkle_root()))  # True


    h = hashlib.sha256("tierion".encode()).hexdigest()
    h4 = hashlib.sha256("hallo123".encode()).hexdigest()
    h2 = hashlib.sha256("bitcoin".encode()).hexdigest()
    h3 = hashlib.sha256("blockchain".encode()).hexdigest()
    print(f"tiercoin: {h}, hallo123 {h4}")
    print(f"bitcoin: {h2}, blockchain: {h3}")

    def validate_proof(proof, target_hash, merkle_root):
        merkle_root = bytearray.fromhex(merkle_root)
        target_hash = bytearray.fromhex(target_hash)
        if len(proof) == 0:
            return target_hash == merkle_root
        else:
            proof_hash = target_hash
            print(proof)
            for p in proof:
                try:
                    # the sibling is a left node
                    sibling = bytearray.fromhex(p['left'])
                    proof_hash = hashlib.sha256(sibling + proof_hash).digest()
                except:
                    # the sibling is a right node
                    sibling = bytearray.fromhex(p['right'])
                    proof_hash = hashlib.sha256(proof_hash + sibling).digest()
            return proof_hash == merkle_root

    # print(validate_proof(mt.get_proof(0), mt.get_leaf(0), mt.get_merkle_root()))

    # sib1 = mt.get_leaf(0)
    # sib2 = mt.get_leaf(1)
    # pf = mt.get_proof(3)
    # print(sib1, sib2)
    # print(pf)
    # sib1 = bytearray.fromhex(sib1)
    # sib2 = bytearray.fromhex(sib2)
    # h = hashlib.sha256(sib1+sib2).digest()
    # t = bytearray.fromhex("a16ed5cdb886809ad9f03e5d717c0087dbb63f31a1b469a0590db417be77167b")
    # print(h == t)
    sibt = bytearray("a16ed5cdb886809ad9f03e5d717c0087dbb63f31a1b469a0590db417be77167b".encode())
    sib1 = bytearray.fromhex("a16ed5cdb886809ad9f03e5d717c0087dbb63f31a1b469a0590db417be77167b")
    sib2 = bytearray.fromhex("0f41ddc98ad685189b3c5b04ac66109467bc9cf77f43fd761ed2cd8fa4b43af7")
    print(sibt, sib1)
    h = hashlib.sha256(sib1+sib2).digest()
    t = bytearray.fromhex(mt.get_merkle_root())
    print(t.hex())

    # proof_hash = "2da7240f6c88536be72abe9f04e454c6478ee29709fc3729ddfb942f804fbf08"
    # sibling = "6b88c087247aa2f07ee1c5956b8e1a9f4c7f892a70e324f1bb3d161e05ca107b"
    # concat = proof_hash+sibling
    # h = hashlib.sha256(concat.encode("utf-8")).hexdigest()
    # print(h)





