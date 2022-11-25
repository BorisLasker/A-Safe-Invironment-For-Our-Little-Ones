
import os
import initial_ast
from ast_test import predict_sample_audio
import audio_test
import cam
from threading import Thread

ADDRESS_FRAME_SAVE = 'ast/audio/'

def AST():
    for root, dirs, files in os.walk(ADDRESS_FRAME_SAVE):
            print("sample_audio_path")
            for _file in files:
                sample_audio_path = _file
                print(sample_audio_path)
                if(predict_sample_audio(initial_ast.audio_model,initial_ast.labels,sample_audio_path)):
                    #create_suspecious_video.Create_Vid(sample_audio_path,100)
                    print(True)
                print(sample_audio_path)
    
#from camera import create_suspecious_video


# counter = 2
# T_audio = audio_test.AudioSample(counter).start()

c = Thread(target=AST(), args=()).start()

# print("sample_audio_path")
# cam.Camera().start()


    



# predict return true if audio is suspeciuos


