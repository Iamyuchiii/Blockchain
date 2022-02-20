from textwrap import wrap
from time import sleep
from wrapper import Wrapper


# settings---------------------------------------------------------------------
network = "local"
typefilter = "sub-sampling"
typestorage = "dropbox"
deploy = False
# base path
basepath = "E:\Blockchain"
# path that the system will scan for greenhouse data
scanpath = f"{basepath}\data_scan"
# path that the modified/original data will be saved
savepath =  f"{basepath}\data_save"
# path in the cloud of which the data can be saved
cloud_path = "/Privacy of Blockchain"
# dropbox token, which is required to use the dropbox
with open("E:\Blockchain\secure_info.txt", "r") as file:
    token = file.read()
# level that can be used to divide the data
ranks = 10
# settings---------------------------------------------------------------------

if __name__ == "__main__":
    while True:
        # network, typefilter, typestorage, scanpath, savepath, ranks, token, cloud_path, deploy=False
        wrapper = Wrapper(network, typefilter, typestorage, scanpath, savepath, ranks, token, cloud_path, deploy)
        wrapper.start2()
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
