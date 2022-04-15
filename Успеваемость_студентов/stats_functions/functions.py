from collections import Counter

def mean(values):
    return sum(values) / len(values)

def standard_deviation(values):
    av = sum(values) / len(values)
    res = 0
    for i in range(len(values)):
        res += (values[i] - av) ** 2
    res /= (len(values) - 1)
    return res ** 0.5

def variance(values):
    av = sum(values) / len(values)
    res = 0
    for i in range(len(values)):
        res += (values[i] - av) ** 2
    res /= (len(values) - 1)
    return res

def kurtosis(values):
    n = len(values)
    stddev = standard_deviation(values)
    av = mean(values)
    res = 0
    for i in range(n):
        res += (values[i] - av) ** 4
    res = res * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * (stddev ** 4))
    res -= 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    return res

def skewness(values):
    n = len(values)
    stddev = standard_deviation(values)
    av = mean(values)
    res = 0
    for i in range(n):
        res += (values[i] - av) ** 3
    res *= n / ((n - 1) * (n - 2) * (stddev ** 3))
    return res

def standard_error(values):
    stddev = standard_deviation(values)
    return stddev / len(values) ** 0.5

def median(values):
    if (len(values) % 2 == 1):
        return sorted(values)[len(values) // 2]
    else:
        ind1 = (len(values) - 1) // 2
        ind2 = ind1 + 2
        return sum(sorted(values)[ind1:ind2]) / 2

def interval(values):
    sorted_values = sorted(values)
    return sorted_values[-1] - sorted_values[0]

def mode(values):
    return Counter(values).most_common(1)[0][0];
