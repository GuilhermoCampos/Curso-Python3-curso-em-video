import os
import random
n = 0
random.seed(),
for root, dirs, files in os.walk('/tmp/foo'):
    for name in files:
        n = n+1
    if random.uniform(0, n) < 1: rfile = os.path.join(root, name)
print(rfile)
