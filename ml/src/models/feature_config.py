from pydantic import BaseModel


class FeatureConfig(BaseModel):
    sample_rate: int = 16000
    n_mels: int = 128
    n_fft: int = 400
    hop_length: int = 160
    f_min: float = 0.0
    f_max: float = 8000.0
