import pickle
import os
from time import sleep
from autodetection import Autodetection
from wrapper import Wrapper


# settings---------------------------------------------------------------------
scanpath = "D:\Blockchain\data_scan"
levels = 10
filename = "test"
savepath = "D:\Blockchain\data_save"
cloud_path = "/Privacy of Blockchain/test.txt"
with open("../secure_info.txt", "r") as file:
    token = file.read()
# settings---------------------------------------------------------------------


def scanmap():
    content = []
    for file in os.listdir("D:\Blockchain\data_scan"):
        if "txt" in file:
            content.append(file)
    return content


if __name__ == "__main__":
    while 1:
        content = scanmap()
        if content:
            for fn in content:
                with open(f"{scanpath}\{fn}", "rb") as file:
                    data = pickle.load(file)
                # data, levels, filename, file_path, token, cloud_path
            wrapper = Wrapper(data, levels, filename, savepath, token, cloud_path)
            wrapper.start()
            os.remove(f"{scanpath}\{fn}")
            sleep(5)
        else:
            print("currently no file in the folder")
            sleep(5)


# # create dummy data
# data = stats.uniform.rvs(size=100, loc=40, scale=80, random_state=9)
# mu, std = stats.norm.fit(data)
# # 1) sorting the data in to different ranks
# datasort = DataSort(data)
# sorted_data = datasort.sortrank(levels)
# # 2) store the data in to txt
# dataprocess = Data_procsseing(sorted_data)
# dataprocess.save_dict_txt(file_name, file_path)
# # 2a) save data to cloud
# dropbox_client = Dropbox_cloudstorage(token)
# dropbox_client.upload_file(f"{file_path}\{file_name}.txt", cloud_path)
# # 3) hashing the data
# merkletree = BuildMerkle(sorted_data).build_merkle()
# rootHash = merkletree.get_merkle_root()
# # hash_dict = {merkletree.get_merkle_root() : [merkletree.get_leaf(i) for i in range(levels)]}
# # # checking for hashes
# # assert merkletree.get_merkle_root() == next(iter(hash_dict))
# # 4) deploy contract
# os.system("brownie run scripts\deploy_local.py --network ganache-local")
# # 4a) store the value
# os.system(
#     f"brownie run scripts\deploy_local.py store_hashes {file_name} {rootHash} --network ganache-local"
# )
