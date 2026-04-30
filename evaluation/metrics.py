import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import rel_entr


class EvaluationEngine:
    def __init__(self, confidence_level=0.95):
        self.confidence_level = confidence_level

    def _align(self, y, ŷ):
        y = np.asarray(y).flatten()
        ŷ = np.asarray(ŷ)

        if ŷ.ndim > 1:
            ŷ = np.mean(ŷ, axis=1)

        n = min(len(y), len(ŷ))
        return y[:n], ŷ[:n]

    def evaluate_all(self, realized, results):
        rows = []

        for name, res in results.items():
            y, ŷ = self._align(realized, res["predictions"])

            rows.append({
                "Model": name,
                "MSE": float(np.mean((ŷ - y) ** 2)),
                "MAE": float(np.mean(np.abs(ŷ - y))),
                "RMSE": float(np.sqrt(np.mean((ŷ - y) ** 2))),
                "Bias": float(np.mean(ŷ - y)),
                "Corr": 0.0 if np.std(y)==0 or np.std(ŷ)==0 else float(np.corrcoef(y, ŷ)[0,1]),
                "Runtime(s)": res.get("runtime", np.nan),
            })

        return pd.DataFrame(rows).set_index("Model")



class StatisticalValidator:

    def _align(self, y, ŷ):
        y = np.asarray(y).flatten()
        ŷ = np.asarray(ŷ)

        if ŷ.ndim > 1:
            ŷ = np.mean(ŷ, axis=1)

        n = min(len(y), len(ŷ))
        return y[:n], ŷ[:n]

    def run_all_tests(self, realized, results):
        rows = []

        for name, res in results.items():
            y, ŷ = self._align(realized, res["predictions"])

            ks_stat, ks_p = stats.ks_2samp(y, ŷ)

            rows.append({
                "Model": name,
                "KS-stat": round(ks_stat, 4),
                "KS-pvalue": round(ks_p, 4),
                "KS-reject": ks_p < 0.05,
            })

        return pd.DataFrame(rows).set_index("Model")
