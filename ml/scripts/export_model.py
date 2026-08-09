import argparse
import os
import sys

import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ml.src.models.vad_model import VADModel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--output_path", type=str, default="model.onnx")
    parser.add_argument("--format", type=str, choices=["onnx", "torchscript"], default="onnx")
    args = parser.parse_args()

    model = VADModel()
    if args.model_path and os.path.exists(args.model_path):
        model.load_state_dict(torch.load(args.model_path))

    model.eval()

    dummy_input = torch.randn(1, 1, 128, 100)

    try:
        if args.format == "onnx":
            torch.onnx.export(
                model,
                dummy_input,
                args.output_path,
                export_params=True,
                opset_version=14,
                do_constant_folding=True,
                input_names=['input_1'],
                output_names=['output_1'],
                dynamic_axes={'input_1': {0: 'batch_size'}, 'output_1': {0: 'batch_size'}}
            )
        else:
            traced_script_module = torch.jit.trace(model, dummy_input)
            traced_script_module.save(args.output_path)
    except Exception:
        traced_script_module = torch.jit.trace(model, dummy_input)
        traced_script_module.save("model.pt")

if __name__ == "__main__":
    main()

