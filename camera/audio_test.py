import pyaudio
import wave
import datetime as dt
import os
import time
from threading import Thread

os.chdir("camera")
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_PATH = "audio/"

class AudioSample:

    def __init__(self,counter):

        self.counter = counter
        self.stopped = False
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.record, args=()).start()
        return self

    def record(self):

        while True:
            if self.stopped:
                self.stream.stop_stream()
                self.stream.close()
                self.p.terminate()
                return 
            self.frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                self.data = self.stream.read(CHUNK)
                self.frames.append(self.data)
            self.store()

    def store(self):
        current_time = dt.datetime.now()
        wf = wave.open(WAVE_OUTPUT_PATH + current_time.strftime('%Y-%m-%d %H-%M-%S') + '.wav', 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        self.counter-=1
        if(self.counter==0):
            self.stop()


    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True



counter = 2
T_audio = AudioSample(counter).start()





# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# frames = []

# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("* done recording")



# stream.stop_stream()
# stream.close()
# p.terminate()

# current_time = dt.datetime.now()


# wf = wave.open(WAVE_OUTPUT_PATH + current_time.strftime('%Y-%m-%d %H-%M-%S') + '.wav', 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()
