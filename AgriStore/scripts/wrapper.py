import os
import shutil
from blockchain_scripts.BuildMerkle import *
from blockchain_scripts.Data_processing import Data_procsseing
from blockchain_scripts.Data_filtering import Datafilter
from blockchain_scripts.Cloudstorage import Dropbox_cloudstorage
import pickle


class Wrapper:
    def __init__(self, scanpath, levels, savepath, token, cloud_path):
        self.scanpath = scanpath
        self.levels = levels
        self.savepath = savepath
        self.token = token
        self.cloud_path = cloud_path

    def scan_map(self):
        """scans file in a given path for txt file as input
        :return: list of file names that ends with txt
        """
        content = []
        for file in os.listdir(self.scanpath):
            if "txt" in file:
                content.append(file.split(".")[0])
        return content

    def start(self, network="local"):
        # 0) get the data
        content = self.scan_map()
        if content:
            for filename in content:
                with open(f"{self.scanpath}\{filename}.txt", "rb") as file:
                    data = pickle.load(file)
                    # 1) sorting the data in to different ranks
                    datasort = Datafilter(data)
                    sorted_data = datasort.sortrank(self.levels)
                    # 2) store the data in to txt
                    dataprocess = Data_procsseing(sorted_data)
                    dataprocess.save_dict_txt(f"{filename}_modified", self.savepath)
                    # 2a) save data to cloud
                    dropbox_client = Dropbox_cloudstorage(self.token)
                    dropbox_client.file_move(
                        f"{self.savepath}\{filename}_modified.txt",
                        f"{self.cloud_path}/{filename}_modified.txt",
                    )
                    # 3) hashing the data
                    merkletree = BuildMerkle(sorted_data).build_merkle()
                    roothash = merkletree.get_merkle_root()
                    if network == "local":
                        # # 4) deploy contract
                        # os.system("brownie run scripts\deploy_local.py --network ganache-local")
                        # 4a) store the value
                        os.system(
                            f"brownie run scripts\deploy_local.py store_hashes {filename} {roothash} --network ganache-local"
                        )
                    elif network == "rinkeby":
                        # # 4) deploy contract
                        # os.system("brownie run scripts\deploy_rinkeby.py --network rinkeby")
                        # 4a) store the value
                        os.system(
                            f"brownie run scripts\deploy_rinkeby.py store_hashes {filename} {roothash} --network rinkeby"
                        )
                    else:
                        raise TypeError("Network not avaible or not in use")
            shutil.move(
                f"{self.scanpath}\{filename}.txt",
                f"{self.savepath}\{filename}.txt",
            )
        else:
            print("currently no file in the folder")


class User:
    def __init__(self):
        pass

    def check_contract(filename, network="local"):
        if network == "local":
            os.system(
                f"brownie run scripts\deploy_local.py check_ledger {filename} --network ganache-local"
            )
        elif network == "rinkeby":
            os.system(
                f"brownie run scripts\deploy_rinkeby.py check_ledger {filename} --network rinkeby"
            )

    def validation(data, hash):
        """check if the received data is still the original"""
        merkle = BuildMerkle(data).build_merkle()
        if hash == merkle.get_merkle_root():
            print(
                f"The current data is still intact\nContract hash: {hash}\nCurrent hash: {merkle.get_merkle_root()}"
            )
        else:
            print(
                f"The current data has been changed\nContract hash: {hash}\nCurrent hash: {merkle.get_merkle_root()}"
            )

    # # step 1
    # def sortingdata(self):
    #     # 1) sorting the data in to different ranks
    #     datasort = DataSort(data)
    #     sorted_data = datasort.sortrank(self.levels)
    #     return sorted_data

    # # step 2
    # def save_to_cloud(self, sorted_data):
    #     # 2) store the data in to txt
    #     dataprocess = Data_procsseing(sorted_data)
    #     dataprocess.save_dict_txt(filename, self.savepath)
    #     # 2a) save data to cloud
    #     dropbox_client = Dropbox_cloudstorage(self.token)
    #     dropbox_client.upload_file(f"{self.savepath}\{filename}.txt", self.cloud_path)

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
    #         f"brownie run scripts\deploy_local.py store_hashes {filename} {roothash} --network ganache-local"
    #     )
