from numpy import pi
import scipy.stats as stats
from blockchain_scripts.Date_privacy import *

data = stats.uniform.rvs(size=100, loc=40, scale=80, random_state=9)
df = PrivacyFilter(data)
print(df.sortrank(10))

with open("E:\Blockchain\data_scan\\dummydata.txt", "w") as file:
    np.savetxt(file, data)
