import numpy as np
from scipy.stats import entropy


class DriftDetector:
    def __init__(self, reference_distribution, threshold=0.1):
        self.reference_distribution = np.array(reference_distribution)
        self.threshold = threshold

    def calculate_kl_divergence(self, current_distribution):
        p = self.reference_distribution / np.sum(self.reference_distribution)
        q = np.array(current_distribution) / np.sum(current_distribution)
        p = np.clip(p, 1e-10, 1.0)
        q = np.clip(q, 1e-10, 1.0)
        kl_div = entropy(p, q)
        return kl_div

    def check_drift(self, current_distribution):
        kl_div = self.calculate_kl_divergence(current_distribution)
        drift_detected = kl_div > self.threshold
        return {
            "drift_detected": bool(drift_detected),
            "kl_divergence": float(kl_div),
            "threshold": self.threshold
        }
