import argparse
import os
import sys

import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ml.src.evaluation.evaluator import Evaluator
from ml.src.models.vad_model import VADModel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--f1_threshold", type=float, default=0.0)
    parser.add_argument("--latency_threshold_ms", type=float, default=500.0)
    args = parser.parse_args()

    model = VADModel()
    if args.model_path and os.path.exists(args.model_path):
        model.load_state_dict(torch.load(args.model_path))

    model.eval()
    
    mock_inputs = torch.randn(100, 1, 128, 100)
    mock_targets = torch.randint(0, 2, (100, 1)).float()
    test_dataset = torch.utils.data.TensorDataset(mock_inputs, mock_targets)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=16)

    evaluator = Evaluator(model, test_loader)
    metrics = evaluator.evaluate()

    if metrics["f1"] < args.f1_threshold:
        sys.exit(1)

    if metrics["avg_latency_ms"] > args.latency_threshold_ms:
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()

