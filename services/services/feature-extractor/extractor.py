import base64

import numpy as np
import torch
import torchaudio


class FeatureExtractor:
    def __init__(self):
        self.mel_transform = torchaudio.transforms.MelSpectrogram(
            sample_rate=16000,
            n_fft=400,
            hop_length=160,
            n_mels=80
        )

    def extract(self, chunk):
        payload_bytes = base64.b64decode(chunk['payload'])
        audio = np.frombuffer(payload_bytes, dtype=np.float32)
        tensor = torch.from_numpy(audio).unsqueeze(0)
        
        melspec = self.mel_transform(tensor)
        features = melspec.squeeze(0).numpy()
        
        out_payload = base64.b64encode(features.tobytes()).decode('utf-8')
        
        return {
            'stream_id': chunk['stream_id'],
            'timestamp_ms': chunk['timestamp_ms'],
            'features': out_payload,
            'shape': list(features.shape)
        }
