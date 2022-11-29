# Get a sample audio and make feature for predict
from initial_ast import make_features
import os, csv, argparse, wget
os.environ['TORCH_HOME'] = '/pretrained_models'
if os.path.exists('pretrained_models') == False:
  os.mkdir('/pretrained_models')
import torch, torchaudio, timm
import numpy as np
from torch.cuda.amp import autocast
import IPython
def predict_sample_audio(audio_model,labels,sample_audio_path):
  #sample_audio_path = "5f651112-d2a3-4911-b3a5-f37bfc092494-1430734627686-1.7-m-72-sc.wav"
  input_tdim = 1024
  feats = make_features(sample_audio_path, mel_bins=128)           # shape(1024, 128)
  feats_data = feats.expand(1, input_tdim, 128)           # reshape the feature
  feats_data = feats_data.to(torch.device("cpu"))
  # do some masking of the input
  #feats_data[:, :512, :] = 0.

  # Make the prediction
  with torch.no_grad():
    with autocast():
      output = audio_model.forward(feats_data)
      output = torch.sigmoid(output)
  result_output = output.data.cpu().numpy()[0]
  sorted_indexes = np.argsort(result_output)[::-1]

  # Print audio tagging top probabilities
  print('Predicted results:')
  for k in range(5):
      print('- {}: {:.4f}'.format(np.array(labels)[sorted_indexes[k]], result_output[sorted_indexes[k]]))
      if(np.array(labels)[sorted_indexes[k]]=='Baby cry, infant cry' and result_output[sorted_indexes[k]]>0.1):
        return True
        
      