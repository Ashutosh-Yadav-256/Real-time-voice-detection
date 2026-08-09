import time

import torch
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


class Evaluator:
    def __init__(self, model, test_loader, device="cpu"):
        self.model = model.to(device)
        self.test_loader = test_loader
        self.device = device

    def evaluate(self):
        self.model.eval()
        all_targets = []
        all_preds = []
        latencies = []

        with torch.no_grad():
            for inputs, targets in self.test_loader:
                inputs = inputs.to(self.device)
                start_time = time.time()
                outputs = self.model(inputs)
                latencies.append(time.time() - start_time)
                preds = (outputs > 0.5).float()
                all_targets.extend(targets.cpu().numpy())
                all_preds.extend(preds.cpu().numpy())

        metrics = {
            "accuracy": accuracy_score(all_targets, all_preds),
            "precision": precision_score(all_targets, all_preds, zero_division=0),
            "recall": recall_score(all_targets, all_preds, zero_division=0),
            "f1": f1_score(all_targets, all_preds, zero_division=0),
            "avg_latency_ms": (sum(latencies) / len(latencies)) * 1000 if latencies else 0
        }
        return metrics
