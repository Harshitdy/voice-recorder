import sounddevice
from scipy.io.wavfile import write

# sample_rate
fs= 44100

second = int(input("Enter the Recording Time in second: "))
print("Recording...")
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=1)
sounddevice.wait()
write("MyRecording.wav", fs, record_voice)
print("Recording is done Please check you folder to listen recording")
