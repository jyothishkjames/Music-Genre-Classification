
__author__  = "Jyothish James"

import os
import sys
import pickle
from pydub import AudioSegment


file_names = []


file_names = [filename.split('.')[0]
              for  filename in os.listdir('/home/jyothish/Downloads/rock')
                if filename.endswith('.mp3')]
             
for i in range(len(file_names)):
    sound = AudioSegment.from_mp3('/home/jyothish/Downloads/rock/'+file_names[i]+'.mp3')
    sound.export('/home/jyothish/Downloads/rock_wav/'+file_names[i]+'.wav', format="wav")





