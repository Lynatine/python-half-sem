import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end = time.perf_counter()
        print("Время выполнения:", end - self.start, "секунд")

with Timer():
    time.sleep(1)
