import initial_ast
from ast_test import predict_sample_audio
import os
from camera import create_suspecious_video


sample_audio_path = "2022-11-22 11-10-17.wav"
# predict return true if audio is suspeciuos
if(predict_sample_audio(initial_ast.audio_model,initial_ast.labels,sample_audio_path)):
    create_suspecious_video.Create_Vid(sample_audio_path,100)

