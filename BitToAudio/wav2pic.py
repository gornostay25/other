import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open('0.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)
Time=np.linspace(0, len(signal)/fs, num=len(signal))
plt.figure(1)
plt.plot(Time,signal)
plt.grid()
plt.savefig("wave")
