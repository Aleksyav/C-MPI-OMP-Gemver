import numpy as np

# proc = [1, 2, 4, 8, 16, 32, 64, 128, 256]
# size = [10000, 4000, 2000, 400, 120, 40]
# test = 5.

proc = [1, 2, 4, 8, 16, 32, 64]
size = [10000, 4000, 2000, 400, 120, 40]
test = 5.

for s in size:
    with open(f"test_{s}_P", "r") as file:
        time = file.readlines()
        time_avg = np.zeros(len(proc), dtype=float)
        for i, t in enumerate(time):
            time_avg[i % len(proc)] += float(t[:-1])
        time_avg /= test
        for t in time_avg:
            print(f"{t}, ", end='')
        print()
