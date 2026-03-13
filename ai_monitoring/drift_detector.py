import numpy as np

class DriftDetector:

    def init(self):
        self.history = []

    def add_prediction(self, confidence):

        self.history.append(confidence)

        if len(self.history) > 100:
            self.history.pop(0)

    def detect_drift(self):

        if len(self.history) < 30:
            return False

        avg = np.mean(self.history)

        if avg < 0.6:
            return True

        return False