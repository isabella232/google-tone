#!/usr/bin/env python
"""Generate a Spectrogram image for a given WAV audio sample.

A spectrogram, or sonogram, is a visual representation of the spectrum
of frequencies in a sound.  Horizontal axis represents time, Vertical axis
represents frequency, and color represents amplitude.
"""

import os
import sys

import ewave
import pylab


def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    file_name, file_ext = os.path.splitext(wav_file)
    
    pylab.savefig('%s.%s' % (file_name, 'png'))


def get_wav_info(wav_file):
    wav = ewave.open(wav_file, 'r')
    frames = wav.read()
    #sound_info = pylab.fromstring(frames, 'Int16')
    sound_info = frames
    frame_rate = wav.sampling_rate
    #wav.close()
    return sound_info, frame_rate


def main(argv):
    wav_file = 'sample.wav' if len(argv) <= 1 else argv[1]
    graph_spectrogram(wav_file)

if __name__ == '__main__':
    main(sys.argv)