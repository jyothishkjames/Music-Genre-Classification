
__author__  = "Jyothish James"


import os
import sys
import pickle


file_names = []

file_names = [filename.split('.')[0]
              for  filename in os.listdir('/home/jyothish/Downloads/jazz_label')
                if filename.endswith('.wav')] 

for i in range(len(file_names)):
    os.rename('/home/jyothish/Downloads/jazz_wav/'+file_names[i]+'.wav', '/home/jyothish/Downloads/alternative_wav/alternative_'+file_names[i]+'.wav')
