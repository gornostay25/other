import math
import wave
import struct

# Audio will contain a long list of samples (i.e. floating point numbers describing the
# waveform).  If you were working with a very long sound you'd want to stream this to
# disk instead of buffering it all in memory list this.  But most sounds will fit in 
# memory.
audio = []
sample_rate = 8000.0
Ma=1
Mi=0.45

def spase(duration_milliseconds=500):
    num_samples = duration_milliseconds * (sample_rate / 1000.0)
    
    for x in range(int(num_samples)): 
        audio.append(0.0)
    
    return

def zero()
def one(d=500):
    duration_milliseconds=d
    """8
    The sine wave generated here is the standard beep.  If you want something
    more aggresive you could try a square or saw tooth waveform.   Though there
    are some rather complicated issues with making high quality square and
    sawtooth waves... which we won't address here :) 
    """ 

    global audio # using global variables isn't cool.

    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(volume)
    spase()
    return


def save_wav(file_name):
    # Open up a wav file
    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1

    sampwidth = 2

    # 44100 is the industry standard sample rate - CD quality.  If you need to
    # save on file size you can adjust it downwards. The stanard for low quality
    # is 8000 or 8kHz.
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))
    for sample in audio:

        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))
    wav_file.close()
    return



f = (open('bits.txt','r')).read()
spase()
for x in f:
    if x == '0':
        one(0.5)    
    elif x == '1':
        one(1)
    else:
        pass
save_wav("0.wav")
