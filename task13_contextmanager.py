import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print("Время выполнения:", end - start, "секунд")

with timer():
    time.sleep(1)
