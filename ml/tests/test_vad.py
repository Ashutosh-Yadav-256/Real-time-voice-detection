import torch
from ml.src.models.vad_model import VADModel

def test_vad_model_forward():
    model = VADModel()
    model.eval()
    dummy_input = torch.randn(2, 1, 128, 100)
    output = model(dummy_input)
    assert output.shape == (2, 1)
