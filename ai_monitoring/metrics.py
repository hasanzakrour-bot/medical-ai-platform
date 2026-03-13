import time

class ModelMetrics:

    def init(self):

        self.inference_times = []

    def start_timer(self):

        return time.time()

    def end_timer(self, start):

        latency = time.time() - start

        self.inference_times.append(latency)

    def average_latency(self):

        if not self.inference_times:
            return 0

        return sum(self.inference_times) / len(self.inference_times)