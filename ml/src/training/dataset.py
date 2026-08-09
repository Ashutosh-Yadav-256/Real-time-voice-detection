import torch
import torchaudio
from torch.utils.data import Dataset


class VADDataset(Dataset):
    def __init__(self, file_paths, labels, config, augmentations=None):
        self.file_paths = file_paths
        self.labels = labels
        self.config = config
        self.augmentations = augmentations
        self.mel_spectrogram = torchaudio.transforms.MelSpectrogram(
            sample_rate=config.sample_rate,
            n_fft=config.n_fft,
            hop_length=config.hop_length,
            n_mels=config.n_mels
        )

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        waveform, sr = torchaudio.load(self.file_paths[idx])
        if sr != self.config.sample_rate:
            resampler = torchaudio.transforms.Resample(sr, self.config.sample_rate)
            waveform = resampler(waveform)
        if self.augmentations:
            waveform = self.augmentations(waveform)
        mel_spec = self.mel_spectrogram(waveform)
        label = torch.tensor([self.labels[idx]], dtype=torch.float32)
        return mel_spec, label
