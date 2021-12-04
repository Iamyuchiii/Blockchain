import os
from blockchain_scripts.BuildMerkle import *
from blockchain_scripts.Data_processing import Data_procsseing
from blockchain_scripts.Data_filtering import DataSort
from blockchain_scripts.Cloudstorage import Dropbox_cloudstorage


class Wrapper:
    def __init__(self, data, levels, filename, file_path, token, cloud_path):
        self.data = data
        self.levels = levels
        self.filename = filename
        self.file_path = file_path
        self.token = token
        self.cloud_path = cloud_path

    def start(self):
        # 1) sorting the data in to different ranks
        datasort = DataSort(self.data)
        sorted_data = datasort.sortrank(self.levels)
        # 2) store the data in to txt
        dataprocess = Data_procsseing(sorted_data)
        dataprocess.save_dict_txt(self.filename, self.file_path)
        # 2a) save data to cloud
        dropbox_client = Dropbox_cloudstorage(self.token)
        dropbox_client.file_move(
            f"{self.file_path}\{self.filename}.txt", self.cloud_path
        )
        # 3) hashing the data
        merkletree = BuildMerkle(sorted_data).build_merkle()
        roothash = merkletree.get_merkle_root()
        # # 4) deploy contract
        # os.system("brownie run scripts\deploy_local.py --network ganache-local")
        # 4a) store the value
        os.system(
            f"brownie run scripts\deploy_local.py store_hashes {self.filename} {roothash} --network ganache-local"
        )

    # # step 1
    # def sortingdata(self):
    #     # 1) sorting the data in to different ranks
    #     datasort = DataSort(self.data)
    #     sorted_data = datasort.sortrank(self.levels)
    #     return sorted_data

    # # step 2
    # def save_to_cloud(self, sorted_data):
    #     # 2) store the data in to txt
    #     dataprocess = Data_procsseing(sorted_data)
    #     dataprocess.save_dict_txt(self.filename, self.file_path)
    #     # 2a) save data to cloud
    #     dropbox_client = Dropbox_cloudstorage(self.token)
    #     dropbox_client.upload_file(f"{self.file_path}\{self.filename}.txt", self.cloud_path)

    # # step 3
    # def hashing_data(self, sorted_data):
    #     # 3) hashing the data
    #     merkletree = BuildMerkle(sorted_data).build_merkle()
    #     roothash = merkletree.get_merkle_root()
    #     # # hash_dict = {merkletree.get_merkle_root() : [merkletree.get_leaf(i) for i in range(levels)]}
    #     # # # checking for hashes
    #     # # assert merkletree.get_merkle_root() == next(iter(hash_dict))
    #     return roothash

    # # step 4
    # def deploy_contract(self):
    #     # 4) deploy contract
    #     os.system("brownie run scripts\deploy_local.py --network ganache-local")

    # def store_value(self, roothash):
    #     # 4a) store the value
    #     os.system(
    #         f"brownie run scripts\deploy_local.py store_hashes {self.filename} {roothash} --network ganache-local"
    #     )
