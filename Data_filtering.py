import scipy.stats as stats

class DataSort():
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
        difference = (max(self.data) - min(self.data))/ranks
        minimum = min(self.data)
        upperscale = minimum + difference
        for i in range(ranks):
            sorted_data[minimum, upperscale] = []
            minimum += difference
            upperscale += difference

        for weight in self.data:
            for key, value in sorted_data.items():
                if weight >= key[0] and weight <= key[1]:
                    value.append(weight)
        # makes tuple keys as string so json dumps can save the dictionary
        sorted_data = {str(key): value for key, value in sorted_data.items()}
        return sorted_data

# if __name__ == "__main__":
#     data = stats.uniform.rvs(size=100, loc = 40, scale = 80)
#     mu, std = stats.norm.fit(data)
#     datasort = DataSort(data)
#     sorted_data = datasort.sortrank(10)
#     print(sorted_data)







