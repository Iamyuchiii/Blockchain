import os.path
from blockchain import *
from Data_processing import Image_processing, Data_procsseing
from Data_filtering import DataSort
from Cloudstorage import Dropbox_cloudstorage
import scipy.stats as stats
import numpy as np
import os

# settings---------------------------------------------------------------------
levels = 10
file_name = "test"
file_path = "D:\Blockchain\data_save"
cloud_path = "DataSave"
# settings---------------------------------------------------------------------

# create dummy data
data = stats.uniform.rvs(size=100, loc=40, scale=80, random_state=9)
mu, std = stats.norm.fit(data)
# sorting the data in to different ranks
datasort = DataSort(data)
sorted_data = datasort.sortrank(levels)
# store the data in to txt
dataprocess = Data_procsseing(sorted_data)
dataprocess.save_dict_txt(file_name, file_path)
# hashing the data
merkletree = BuildMerkle(sorted_data).build_merkle()
rootHash = merkletree.get_merkle_root()
# hash_dict = {merkletree.get_merkle_root() : [merkletree.get_leaf(i) for i in range(levels)]}
# # checking for hashes
# assert merkletree.get_merkle_root() == next(iter(hash_dict))
# deploy contract
os.system("cd AgriStore")
os.system("brownie run scripts\deploy_local.py")


# def wrapper():
#     blockchain = Blockchain()
#     data = input("What data will be added?\n")
#     while data.lower() != "stop":
#         mt = None
#         # processing data
#         if os.path.exists(data):
#             processing = Image_processing(data, type="image")
#             image_hashlist = processing.data_type()
#             mt = BuildMerkle(image_hashlist).merkle_tree
#         elif data[0] == "{" and data[-1] == "}":
#             data = json.loads(data)
#             mt = BuildMerkle(data).merkle_tree
#         else:
#             raise Exception("file type not supported")
#         blockchain.add_info(mt)
#         print(blockchain.getlastblock())
#         data = input("What new data will be added?\n")
#
# wrapper()

# # image data
# {"test":"hallo", "test2":"hall3"}
# "D:\\Blockchain\\test_data\\test"
# laptop = "D:\master_thesis\Blockchain"
# computer = r"D:\Blockchain\test_data\test"
# # string data
# data = {
#     "input" : "asdasdasd",
#     "output" : "assdasdasdasd"
# }
# # processing data
# processing = Data_processing(computer, type="image")
# image_hashlist = processing.data_type()
# # building merkletree
# mt = BuildMerkle(image_hashlist).merkle_tree
# mt2 = BuildMerkle(data).merkle_tree
# # # adding blocks
# chain = Blockchain()
# chain.add_info(mt)
# chain.add_info(mt2)
# for i in chain.blocks:
#     print(i)
