from numpy import pi
import scipy.stats as stats
import pickle
from blockchain_scripts.Data_filtering import *

data = stats.uniform.rvs(size=100, loc=40, scale=80, random_state=9)
df = Datafilter(data)
print(df.sortrank(10))

with open("D:\Blockchain\data_scan\\dummydata2.txt") as file:
    pickle.dump(data, file)
