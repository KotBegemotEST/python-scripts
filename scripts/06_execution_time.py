import time
import random


class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time


# ---- run code ---- #

timer = ExecutionTime()
sample_list = []

for num in range(1, 1000000):
    if num % 2 == 0:
        random_number = random.randint(1, 888898)
        sample_list.append(random_number)

print('Finished in {} seconds.'.format(timer.duration()))
