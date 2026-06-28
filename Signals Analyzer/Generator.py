# This file includes all the functions used to store functions storing signal-generating fuhnctions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sine_continuous(frequency, amplitude, phase=0, duration=1, sample_space=100):
    # Generates a Continuous Sine wave with the given frequency, amplitude, phase (default 0), duration (default 1 sec) and sample space (default 100)
    # Stores it as a numpy array
    timestamps = np.linspace(0,duration,sample_space)
    SineWave = amplitude * np.sin(2 * np.pi *frequency * timestamps + phase)
    return np.round(SineWave, decimals=10)

def sine_discrete(frequency, amplitude, phase=0, N=20):
    # Generates a Discrete Sine wave with the given frequency, amplitude, phase (default 0), duration (default 1 sec) and sample space (default 100)
    # Stores it as a numpy array
    timestamps = np.linspace(0,N,N+1)
    SineWave = amplitude * np.sin(2 * np.pi *frequency * timestamps + phase)
    return np.round(SineWave, decimals=10)

def cosine_continuous(frequency, amplitude, phase=0, duration=1, sample_space=100):
    # Generates a Cosine wave with the given frequency, amplitude, phase (default 0), duration (default 1 sec) and sample space (default 100)
    # Stores it as a numpy array
    timestamps = np.linspace(0,duration,sample_space)
    CosineWave = amplitude * np.cos(2 * np.pi *frequency * timestamps + phase)
    return np.round(CosineWave, decimals=10)

def cosine_discrete(frequency, amplitude, phase=0, N=20):
    # Generates a Discrete Cosine wave with the given frequency, amplitude, phase (default 0), duration (default 1 sec) and sample space (default 100)
    # Stores it as a numpy array
    timestamps = np.linspace(0,N,N+1)
    CosineWave = amplitude * np.cos(2 * np.pi *frequency * timestamps + phase)
    return np.round(CosineWave, decimals=10)