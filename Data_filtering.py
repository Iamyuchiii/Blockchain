import scipy.stats as stats

data = stats.uniform.rvs(size=100, loc = 40, scale = 80)
mu, std = stats.norm.fit(data)
average = sum(data)/len(data)

def make_ranks(data, levels):
    sorted_data = {}
    difference = (max(data) - min(data))/levels
    minimum = min(data)
    upperscale = minimum + difference
    for i in range(levels):
        sorted_data[minimum, upperscale] = []
        minimum += difference
        upperscale += difference

    for weight in data:
        for key, value in sorted_data.items():
            if weight >= key[0] and weight <= key[1]:
                value.append(weight)

    return sorted_data

sorted = make_ranks(data, 10)
print(sorted)










