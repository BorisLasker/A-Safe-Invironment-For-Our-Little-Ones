import pyaudio
import wave
import datetime as dt
import os
import time
from threading import Thread
import shutil
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 10
WAVE_OUTPUT_PATH = "audio/"
WAVE_OUTPUT = "./"
import cam 




class AudioSample:

    def __init__(self):
        print('mic is on')
        # self.counter = counter
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
            shutil.move('./' + self.audioname[2:], WAVE_OUTPUT_PATH)
    def store(self):
        current_time = dt.datetime.now()
        self.audioname = WAVE_OUTPUT + current_time.strftime('%Y-%m-%d %H-%M-%S') + '.wav'
        wf = wave.open(self.audioname , 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        if(cam.FlagMicStop):
            print('mic is off')
            self.stop()


    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
        
# AudioSample().start()
