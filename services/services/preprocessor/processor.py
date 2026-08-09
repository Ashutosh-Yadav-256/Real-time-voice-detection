import base64

import numpy as np
import scipy.signal


class AudioProcessor:
    def __init__(self, target_sr=16000):
        self.target_sr = target_sr

    def process(self, chunk):
        payload_bytes = base64.b64decode(chunk['payload'])
        audio = np.frombuffer(payload_bytes, dtype=np.int16).astype(np.float32)
        
        orig_sr = chunk.get('sample_rate', 16000)
        if orig_sr != self.target_sr:
            num_samples = int(len(audio) * self.target_sr / orig_sr)
            audio = scipy.signal.resample(audio, num_samples)
            
        max_val = np.max(np.abs(audio))
        if max_val > 0:
            audio = audio / max_val
            
        energy = np.sum(audio ** 2) / len(audio)
        if energy < 1e-4:
            return None
            
        out_payload = base64.b64encode(audio.tobytes()).decode('utf-8')
        
        return {
            'stream_id': chunk['stream_id'],
            'timestamp_ms': chunk['timestamp_ms'],
            'payload': out_payload,
            'format': 'float32',
            'sample_rate': self.target_sr,
            'channels': 1
        }
