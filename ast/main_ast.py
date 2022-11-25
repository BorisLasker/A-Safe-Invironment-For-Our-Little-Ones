
import os
import initial_ast
from ast_test import predict_sample_audio
import audio_test
import cam
from threading import Thread

ADDRESS_FRAME_SAVE = 'audio/'

def AST():
    for root, dirs, files in os.walk(ADDRESS_FRAME_SAVE):
            for _file in files:
                sample_audio_path = _file
                print(sample_audio_path)
                if(predict_sample_audio(initial_ast.audio_model,initial_ast.labels,ADDRESS_FRAME_SAVE+sample_audio_path)):
                    #create_suspecious_video.Create_Vid(sample_audio_path,100)
                    print(True)
    
#from camera import create_suspecious_video



cam.Camera().start()
T_audio = audio_test.AudioSample().start()


Thread(target = AST(), args=()).start()



#sample_audio_path='audio/2022-11-25 10-17-55.wav'
#predict_sample_audio(initial_ast.audio_model,initial_ast.labels,sample_audio_path)



    



# predict return true if audio is suspeciuos


