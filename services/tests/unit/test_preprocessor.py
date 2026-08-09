import unittest

import numpy as np


def preprocess(audio_data, target_sr=16000):
    if not isinstance(audio_data, np.ndarray):
        raise TypeError("Input must be a numpy array")
    if audio_data.ndim > 1:
        audio_data = audio_data.mean(axis=1)
    if len(audio_data) == 0:
        return np.zeros(target_sr)
    return audio_data / (np.max(np.abs(audio_data)) + 1e-8)

class TestPreprocessor(unittest.TestCase):
    def test_stereo_to_mono(self):
        audio = np.random.randn(32000, 2)
        result = preprocess(audio)
        self.assertEqual(result.ndim, 1)

    def test_empty_audio(self):
        audio = np.array([])
        result = preprocess(audio)
        self.assertEqual(len(result), 16000)

    def test_normalization(self):
        audio = np.array([1.0, 2.0, 3.0, -4.0])
        result = preprocess(audio)
        self.assertAlmostEqual(np.max(np.abs(result)), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
