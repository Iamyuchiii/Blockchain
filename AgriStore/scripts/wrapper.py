import os
import shutil
from brownie import Contract
from numpy import loadtxt
from blockchain_scripts.BuildMerkle import *
from blockchain_scripts.Data_processing import *
from blockchain_scripts.Date_privacy import PrivacyFilter
from blockchain_scripts.Cloudstorage import Dropbox_cloudstorage
from blockchain_scripts.Cloudstorage import ipfs


class Wrapper:
    def __init__(self, network, typefilter, typestorage, scanpath, savepath, ranks, token, cloud_path, deploy=False):
        # Options of which the system uses (optional path)
        self.network = network
        self.typefilter = typefilter
        self.typestorage = typestorage
        self.scanpath = scanpath
        self.savepath = savepath
        self.ranks = ranks
        self.token = token
        self.cloud_path = cloud_path
        self.deploy = deploy
        # file extentions
        self.tekst_data = (".txt")
        self.image_data = (".png", ".jpeg")

    def scan_map(self):
        """scans file in a given path for txt file as input
        :return: list of file names that ends with txt
        """
        valid_extentions = (".txt", ".png", ".jpeg", ".jpg")
        files = []
        for file in os.listdir(self.scanpath):
            if file.lower().endswith(valid_extentions):
                files.append(file)
        return files

    def data_privacy(self, filename, data):
        """adds privacy according to the users choice
        """
        privacy_scripts = PrivacyFilter(data)
        if self.typefilter == "sub-sampling":
            modified_data = privacy_scripts.sortrank(self.ranks)
            dataprocess = Data_procsseing(modified_data)
            dataprocess.save_dict_txt(f"modified_{filename}", self.savepath)
            
        elif self.typefilter == "laplace":
            modified_data = privacy_scripts.exponential_noise()
            dataprocess = Data_procsseing(modified_data)
            dataprocess.save_dict_txt(f"modified_{filename}", self.savepath)

        else:
            print(f"This option is not supported: {self.typefilter}")

        return modified_data

    def cloud_storage(self, filename):
        """adds files to the storage according to the users choice
        """
        if self.typestorage == "dropbox":
            dropbox_client = Dropbox_cloudstorage(self.token)
            dropbox_client.file_move(
                f"{self.savepath}\{filename}",
                f"{self.cloud_path}/{filename}",
            )
        elif self.typestorage == "google":
            pass
        elif self.typestorage == "ipfs":
            pass

    def data_hashing(self, data):
        merkletree = BuildMerkle(data).build_merkle()
        roothash = merkletree.get_merkle_root()
        return roothash

    def image_hash(self, image):
        hash_scripts = Image_hash(image)
        hash = hash_scripts.image_hasing()
        return hash

    def contract_interaction(self, filename, hash):
        if self.network == "local":
            os.system(
                f"brownie run scripts\deploy_local.py store_hashes {filename} {hash} --network ganache-local"
            )
        elif self.network == "rinkeby":
            os.system(
                f"brownie run scripts\deploy_rinkeby.py store_hashes {filename} {hash} --network rinkeby"
            )
        else:
            raise TypeError("Network not avaible or not in use")
    
    def deploy_contract(self):
        if self.network == "local":
            os.system(
                f"brownie run scripts\deploy_local.py deploy_greenhouseStorage --network ganache-local"
            )
        elif self.network == "rinkeby":
            os.system(
                f"brownie run scripts\deploy_rinkeby.py deploy_contract --network rinkeby"
            )
        else:
            raise TypeError("Network not avaible or not in use")

    def start(self):
        hash = ""
        # deploy contract if needed the options is selected
        if self.deploy == True:
            self.deploy_contract()

        # start the pipeline
        content = self.scan_map()
        if content:
            for filename in content:
                if filename.lower().endswith(self.image_data):
                    hash = self.image_hash()
                    self.cloud_storage(filename)

                elif filename.lower().endswith(self.tekst_data):
                    with open(f"{self.scanpath}\{filename}", "rb") as file:
                        data = loadtxt(file)
                        modified_data = self.data_privacy(filename, data)
                        hash = self.data_hashing(modified_data)
                        self.cloud_storage(f"modified_{filename}")
                        
                self.contract_interaction(filename, hash)
                shutil.move(
                            f"{self.scanpath}\{filename}",
                            f"{self.savepath}\{filename}",
                        )
        else:
            print("currently no file in the folder")

class Wrapper2:
    def __init__(self, rootpath, sensitivity, epsilon, scanpath, savepath, network, deploy=False):
        self.rootpath = rootpath
        self.scanpath = scanpath
        self.savepath = savepath
        self.sensitivity = sensitivity 
        self.epsilon = epsilon
        self.network = network
        self.deploy = deploy
        # file extentions
        self.tekst_data = (".txt")
        self.image_data = (".png", ".jpeg")

    def scan_map(self):
        """scans file in a given path for txt file as input
        :return: list of file names that ends with txt
        """
        valid_extentions = (".txt", ".png", ".jpeg", ".jpg")
        files = []
        for file in os.listdir(self.scanpath):
            if file.lower().endswith(valid_extentions):
                files.append(file)
        return files

    def data_privacy(self, filename, data):
        privacy_scripts = PrivacyFilter(data)
        modified_data = privacy_scripts.laplacian_noise2(sensitivity=self.sensitivity, epsilon=self.epsilon)
        dataprocess = Data_procsseing(modified_data)
        dataprocess.save_dict_txt(f"modified_{filename}", self.savepath)
        return modified_data

    def IPFS(self):
        IPFS = ipfs(self.savepath, self.rootpath)
        hash = IPFS.uploadfile()
        return hash

    def contract_interaction(self, filename, hash):
        if self.network == "local":
            os.system(
                f"brownie run scripts\deploy_local.py store_hashes {filename} {hash} --network ganache-local"
            )
        elif self.network == "rinkeby":
            os.system(
                f"brownie run scripts\deploy_rinkeby.py store_hashes {filename} {hash} --network rinkeby"
            )
        else:
            raise TypeError("Network not avaible or not in use")
    
    def deploy_contract(self):
        if self.network == "local":
            os.system(
                f"brownie run scripts\deploy_local.py deploy_greenhouseStorage --network ganache-local"
            )
        elif self.network == "rinkeby":
            os.system(
                f"brownie run scripts\deploy_rinkeby.py deploy_contract --network rinkeby"
            )
        else:
            raise TypeError("Network not avaible or not in use")

    def start(self):
        hash = ""
        # deploy contract if needed the options is selected
        if self.deploy == True:
            self.deploy_contract()

        # start the pipeline
        content = self.scan_map()
        if content:
            for filename in content:
                print(filename)
                with open(f"{self.scanpath}\{filename}", "rb") as file:
                    data = loadtxt(file)
                    self.data_privacy(filename, data)
                    hash = self.IPFS()
                    self.contract_interaction(filename, hash)
                shutil.move(
                            f"{self.scanpath}\{filename}",
                            f"{self.savepath}\{filename}",
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

