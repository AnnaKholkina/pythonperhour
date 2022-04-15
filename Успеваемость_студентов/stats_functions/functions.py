from collections import Counter
from typing import List
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import matplotlib.pyplot as plt
import matplotlib


def is_numeric_array(values: List[float]) -> bool:
    assert len(values) != 0, "Пустое множество"
    
    for elem in values:
        if not isinstance(elem, (int, float)) or isinstance(elem, bool):
            return False
    
    return True


def mean(values: List[float]) -> float:
    assert len(values) != 0, "Пустое множество"
    
    return sum(values) / len(values)


def variance(values: List[float]) -> float:
    assert len(values) != 0, "Пустое множество"
    
    if len(values) == 1:
        return 0
    
    av = mean(values)
    res = 0
    for i in range(len(values)):
        res += (values[i] - av) ** 2
    res /= (len(values) - 1)
    return res


def standard_deviation(values: List[float]) -> float:
    return variance(values) ** 0.5


def kurtosis(values: List[float]) -> float:
    assert len(values) != 0, "Пустое множество"
    
    if len(values) <= 3:
        return 0
    
    n = len(values)
    stddev = standard_deviation(values)
    av = mean(values)
    res = 0
    for i in range(n):
        res += (values[i] - av) ** 4
    res = res * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * (stddev ** 4))
    res -= 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    return res


def skewness(values: List[float]) -> float:
    assert len(values) != 0, "Пустое множество"
    
    if len(values) <= 2:
        return 0
    
    n = len(values)
    stddev = standard_deviation(values)
    av = mean(values)
    res = 0
    for i in range(n):
        res += (values[i] - av) ** 3
    res *= n / ((n - 1) * (n - 2) * (stddev ** 3))
    return res


def standard_error(values: List[float]) -> float:
    assert len(values) != 0, "Пустое множество"
    
    stddev = standard_deviation(values)
    return stddev / len(values) ** 0.5


def median(values: List[float]) -> float:
    assert len(values) != 0, "Пустое множество"
    
    if (len(values) % 2 == 1):
        return sorted(values)[len(values) // 2]
    else:
        ind1 = (len(values) - 1) // 2
        return sum(sorted(values)[ind1:ind1 + 2]) / 2

    
def quantile(values: List[float], p: float = 0.5) -> float:
    assert len(values) != 0, "Пустое множество"
    
    p_index = int(p * (len(values) - 1))
        
    return sorted(values)[p_index]


def interval(values: List[float]) -> float:
    if len(values) == 0:
        return 0
    
    return max(values) - min(values)


def mode(values: List[float]) -> List[float]:
    assert len(values) != 0, "Пустое множество"
    
    counts = Counter(values)
    max_count = max(counts.values())
    
    if all(1 if count == max_count else 0 for value, count in counts.items()):
        return []
    
    return [value for value, count in counts.items()
            if count == max_count]


def covariance(values_1: List[float], values_2: List[float]) -> float:
    assert len(values_1) != 0 and len(values_2) != 0, "Пустое множество"
    
    num_of_values = min(len(values_1), len(values_2))
    if num_of_values == 1:
        return 0
    
    mean1 = mean(values_1)
    mean2 = mean(values_2)
    covariance = 0
    for i in range(num_of_values):
        covariance += (values_1[i] - mean1) * (values_2[i] - mean2)
    return covariance / (num_of_values - 1)


def correlation(values_1: List[float], values_2: List[float]) -> float:
    assert len(values_1) != 0 and len(values_2) != 0, "Пустое множество"
    
    covar = covariance(values_1, values_2)
    stddev1 = standard_deviation(values_1)
    stddev2 = standard_deviation(values_2)
    if stddev1 > 0 and stddev2 > 0:
        return covar / (stddev1 * stddev2)
    else:
        return 0


def graph_bar_percentage(xs: List[float], ys: List[float], plot: bool = False,
                         title: str = "", xlabel: str = "", ylabel: str = "", 
                         save: bool = False, savename: str = ""):
    assert len(xs) != 0, "Пустая абсцисса графика"
    
    cnt = Counter(ys)
    ys = [cnt[x] / len(ys) * 100 for x in xs]
    plt.figure(figsize = (12, 7))
    plt.bar(xs, ys, color = "silver", edgecolor = "dimgrey", linewidth = 3, alpha = 0.9)
    if plot:
        xnew = np.linspace(min(xs), max(xs), 100)
        spl = make_interp_spline(xs, ys, k = 3)
        ynew = spl(xnew)
        plt.plot(xnew, ynew, color = "dimgray", linewidth = 4)
    if (title != ""):
        plt.title(title, size = 14, family = "serif", alpha = 0.85, weight = "heavy")
    if xlabel != "":
        plt.xlabel(xlabel, size = 14, family = "serif", alpha = 0.85)
    if ylabel != "":
        plt.ylabel(ylabel, size = 14, family = "serif", alpha = 0.85)
    plt.axis([xs[0] - 0.5, xs[-1] + 0.5, 0, max(ys) * 1.1]);
    plt.xticks(xs)
    plt.yticks(range(0, int(max(ys)) + 10, 10))
    if save:
        if savename != "":
            plt.savefig(savename)
        else:
            plt.savefig(title)
    plt.show()


def graph_correlation_map(correlation_matrix: List[List[float]], 
                          vmin: float = -1, vmax: float = 1,
                          labels: List[str] = [], title: str = "",
                          save: bool = False, savename: str = ""):
    assert len(correlation_matrix) != 0, "Пустая матрица корреляции"
    
    fig, ax = plt.subplots(figsize = (12, 12))
    im = ax.imshow(correlation_matrix, cmap = "coolwarm", vmin = vmin, vmax = vmax)

    if labels != []:
        ax.set_xticks(np.arange(len(labels)), labels = labels, size = 10)
        ax.set_yticks(np.arange(len(labels)), labels = labels, size = 10)

    plt.setp(ax.get_xticklabels(), rotation = 30, ha = "right",
         rotation_mode="anchor")

    for i in range(len(correlation_matrix)):
        for j in range(len(correlation_matrix)):
            text = ax.text(j, i, round(correlation_matrix[i][j], 2),
                           ha="center", va="center", color="w", size = 12)
    
    cbar = ax.figure.colorbar(im, ax = ax, shrink = 0.64)
    cbar.ax.set_ylabel("Значение корреляции", rotation=90, va="bottom",
                       size = 14, family = "serif", alpha = 0.85, weight = "heavy")
    
    if title != "":
        ax.set_title(title, size = 18, alpha = 0.85, weight = "heavy")
    fig.tight_layout()
    if save:
        if savename != "":
            plt.savefig(savename)
        else:
            plt.savefig(title)
    plt.show()
    
