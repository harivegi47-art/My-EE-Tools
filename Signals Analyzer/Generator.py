# This file includes all the functions used to store functions storing signal-generating fuhnctions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sine(frequency, amplitude, phase=0, duration=1, sample_space=100):
    # Generates a Sine wave with the given frequency, amplitude, phase (default 0), duration (default 1 sec) and sample space (default 100)
    # Stores it as a numpy array
    timestamps = np.linspace(0,duration,sample_space)
    SineWave = amplitude * np.sin(2 * np.pi *frequency * timestamps + phase)
    return SineWave