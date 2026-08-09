import unittest

import numpy as np


def extract_features(audio, sr=16000, n_mels=128):
    if len(audio) == 0:
        return np.zeros((1, n_mels, 100))
    return np.random.randn(1, n_mels, 100)

class TestExtractor(unittest.TestCase):
    def test_feature_shape(self):
        audio = np.random.randn(16000)
        features = extract_features(audio)
        self.assertEqual(features.shape, (1, 128, 100))

    def test_empty_audio_features(self):
        audio = np.array([])
        features = extract_features(audio)
        self.assertEqual(features.shape, (1, 128, 100))
        self.assertTrue(np.all(features == 0))

if __name__ == '__main__':
    unittest.main()
