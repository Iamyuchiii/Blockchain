from textwrap import wrap
from time import sleep
from wrapper import Wrapper
from wrapper import Wrapper2
import os

# rootpath
rootpath = os.path.abspath(__file__).rsplit("\\", 3)[0]
# path that the system will scan for greenhouse data
scanpath = f"{rootpath}\data_scan"
# path that the modified/original data will be saved
savepath =  f"{rootpath}\data_save"
# which blockchain network to use (local, rinkeby)
network = "local"
# whether to deploy a new contract or not
deploy = False
# chose which path to use (optional or main)
path = "main"

# other settings---------------------------------------------------------------------
sensitivity = 1
epsilon = 1
typefilter = "sub-sampling"
typestorage = "dropbox"
# path in the cloud of which the data can be saved
cloud_path = "/Privacy of Blockchain"
# dropbox token, which is required to use the dropbox (save the token in secure_info.txt)
with open(f"{rootpath}\secure_info.txt", "r") as file:
    token = file.read()
# level that can be used to divide the data
ranks = 10
# other settings---------------------------------------------------------------------

if __name__ == "__main__":
    while True:
        if path == "optional":
            # network, typefilter, typestorage, scanpath, savepath, ranks, token, cloud_path, deploy=False
            wrapper = Wrapper(network, typefilter, typestorage, scanpath, savepath, ranks, token, cloud_path, deploy)
            wrapper.start()
            sleep(5)
            
        elif path == "main":
            wrapper2 = Wrapper2(rootpath,sensitivity, epsilon, scanpath, savepath, network, deploy)
            wrapper2.start()
            sleep(5)
