import numpy as np
import pandas as pd
from diffprivlib.mechanisms import *
import matplotlib.pyplot as plt


class PrivacyFilter:
    def __init__(self, data):
        """Class for sorting datas
        :param data:
        """
        self.data = data

    def sortrank(self, ranks):
        """divide numbers into selected ranks and place and numbers insde the
        ranks.
        :param ranks: number of ranks
        :return: a dictionary containing sorted ranks
        """
        sorted_data = {}
        difference = (max(self.data) - min(self.data)) / ranks
        lowerscale = min(self.data)
        upperscale = lowerscale + difference
        for i in range(ranks):
            sorted_data[lowerscale, upperscale] = []
            lowerscale += difference
            upperscale += difference

        for weight in self.data:
            for key, value in sorted_data.items():
                if weight >= key[0] and weight <= key[1]:
                    value.append(weight)
        # makes tuple keys as string so json dumps can save the dictionary
        sorted_data = {str(key): value for key, value in sorted_data.items()}
        return sorted_data

    def laplacian_noise2(self, epsilon=1, sensitivity=1, roundNumber=False):
        noise_data = []
        lower = min(self.data)*0.8
        upper = max(self.data)*1.2
        laplace = LaplaceTruncated(epsilon=epsilon, sensitivity=sensitivity, lower=lower, upper=upper)
        for i in self.data:
            adding_noise = laplace.randomise(i)
            if roundNumber:
                noise_data.append(round(adding_noise))
            else:
                noise_data.append(adding_noise)
        return noise_data

    def laplacian_noise(self, location=1, sensitivity=1, epsilon=1):
        """Adding laplacian noise over the entire dataset
        :param location: mu, default = 1
        :param sensitivity: depending on the query and database, default = 1
        :param epsilon: privacy budget, default = 1
        :return: data with additive noise
        """
        # sensitivity is dependent on the database + query (for count query sensitivity = 1)
        # epsilon = sensitivity budget
        scale = sensitivity / epsilon
        laplacian_noise = np.random.laplace(location, scale, len(self.data))
        noisydata = laplacian_noise + self.data
        return noisydata

    def exponential_noise(self, maxlimit=1):
        """Adding exponential noise over the entire dataset
        :param maxlimit:
        """
        exponential_noise = np.random.exponential(maxlimit)
        noisydata = self.data + exponential_noise
        return noisydata


class Benchmark:
    def laplacian_sensitivity(noisydata, originaldata):
        return max(abs(noisydata - originaldata))

    def rmse(prediction, target):
        return np.sqrt(((prediction - target) ** 2).mean())

# data = pd.read_pickle("D:\Blockchain\dummydata.txt")
# print(data)
# addnoise = Datafilter(data)
# noisydata = addnoise.laplacian_noise(epsilon=0.1)
# noisydataexpo = addnoise.exponential_noise()
# average = data.mean()
# naverage = noisydata.mean()
# print(average, naverage)

# data = pd.read_pickle("D:\Blockchain\dummydata.txt")
# epsilon = 0.1
# average = data.mean()
# lower = min(data)
# upper = max(data)
# count = len(data)
# anoymizer = DiffPrivLaplaceMechanism(epsilon)
# anoymized = anoymizer.anonymize_mean(average, lower, upper, count)
# print(average, anoymized)
