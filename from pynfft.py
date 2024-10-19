from pynfft.nfft import NFFT
import numpy as np
plan = NFFT([16, 16], 92)
print(plan.M)
print(plan.N)

x = ([1 ,2, 3, 4])

plan.x = x