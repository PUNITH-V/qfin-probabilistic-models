import numpy as np
from scipy.stats import ks_2samp

class StatisticalValidator:
    def __init__(self):
        pass

    def ks_test(self, a, b):
        # Kolmogorov-Smirnov test
        stat, p_value = ks_2samp(a, b)
        return {
            "KS Statistic": stat,
            "p-value": p_value
        }

    def compare_means(self, a, b):
        return {
            "mean_a": np.mean(a),
            "mean_b": np.mean(b),
            "difference": np.mean(a) - np.mean(b)
        }
