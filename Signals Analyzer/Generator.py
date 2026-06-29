# This file includes all the functions used to store functions storing signal-generating functions
import math
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
    xpoints = np.linspace(0,N,N+1)
    SineWave = amplitude * np.sin(2 * np.pi *frequency * xpoints + phase)
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
    xpoints = np.linspace(0,N,N+1)
    CosineWave = amplitude * np.cos(2 * np.pi *frequency * xpoints + phase)
    return np.round(CosineWave, decimals=10)

def Exponential_real_continous(C, a, duration=1, sample_space=100):
    #Generates an Real Continous Exponential signal in the form C(e^(a*t)) for a given duration
    #stores it as numpy array
    timestamps = np.linspace(0,duration,sample_space)
    ExpoSignal = C * pow(math.e, a*timestamps)
    return np.round(ExpoSignal, decimals=10)

def Exponential_real_discrete(C, alpha, N=20):
    #Generates an Real Discrete Exponential signal in the form C(e^(a*t)) for a given duration
    #stores it as numpy array
    xpoints = np.linspace(0,N,N+1)
    ExpoSignal = C * pow(alpha, xpoints)
    return np.round(ExpoSignal, decimals=10)