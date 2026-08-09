import random

import torch
import torchaudio.transforms as T


class AudioAugmentation:
    def __init__(self, noise_std=0.01, rate_range=(0.8, 1.2), steps_range=(-4, 4)):
        self.noise_std = noise_std
        self.rate_range = rate_range
        self.steps_range = steps_range

    def __call__(self, waveform):
        if random.random() > 0.5:
            noise = torch.randn_like(waveform) * self.noise_std
            waveform = waveform + noise
        
        if random.random() > 0.5:
            rate = random.uniform(*self.rate_range)
            time_stretch = T.TimeStretch(hop_length=160, n_freq=201)
            spectrogram = T.Spectrogram(n_fft=400)(waveform)
            stretched = time_stretch(spectrogram, rate)
            waveform = T.GriffinLim(n_fft=400)(stretched)
            
        if random.random() > 0.5:
            steps = random.randint(*self.steps_range)
            pitch_shift = T.PitchShift(sample_rate=16000, n_steps=steps)
            waveform = pitch_shift(waveform)

        return waveform
