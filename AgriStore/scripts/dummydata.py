from numpy import pi
import scipy.stats as stats
import pickle

data = stats.uniform.rvs(size=100, loc=40, scale=80, random_state=9)

with open("D:\Blockchain\data_scan\\dummydata.txt", "wb") as file:
    pickle.dump(data, file)
