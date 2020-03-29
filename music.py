from pydub import AudioSegment  #ffmpeg must be installed
import librosa
import numpy as np

src = "All.mp3"
dst = "test.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

filename = librosa.load()
y, sr = librosa.load(filename, sr=None)
print(y.shape, sr)  #the sampling rate of y, the number of samples per second of audio

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print(beat_times)

y_harmonic, y_percussive = librosa.effects.hpss(y)
chromagram = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)
hop_length = 512  # надо разобраться с этим параметром
beat_chroma = librosa.util.sync(chromagram,beat_frames, aggregate=np.median)  #np.max(), np.min(), np.std(), etc.

mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)
mfcc_delta = librosa.feature.delta(mfcc)
beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]),
                                    beat_frames)
beat_features = np.vstack([beat_chroma, beat_mfcc_delta])
print((beat_features))