import os.path
from blockchain import *
from Data_processing import *

def wrapper():
    blockchain = Blockchain()
    data = input("What data will be added?\n")
    while data.lower() != "stop":
        mt = None
        # processing data
        if os.path.exists(data):
            processing = Data_processing(data, type="image")
            image_hashlist = processing.data_type()
            mt = BuildMerkle(image_hashlist).merkle_tree
        elif data[0] == "{" and data[-1] == "}":
            data = json.loads(data)
            mt = BuildMerkle(data).merkle_tree
        else:
            raise Exception("file type not supported")
        blockchain.add_info(mt)
        print(blockchain.getlastblock())
        data = input("What new data will be added?\n")

wrapper()

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