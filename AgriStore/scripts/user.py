import json
from wrapper import User

user = User.check_contract("dummydata")
with open("D:\Blockchain\data_save\dummydata_modified.txt") as file:
    data = json.load(file)
validation = User.validation(
    data, "7854fbe507ef66ed1fe49a8828072ffb3240f234b91b463a8ea7c9593be95957"
)
