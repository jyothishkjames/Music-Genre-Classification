
__author__  = "Jyothish James"


import scipy.io.wavfile 
import numpy as np
from scikits.talkbox.features import mfcc
import numpy
import os
import sys
import pickle
from nnsearch import NearestNeighborSearch
from simsearch import SimilaritySearch

file_names = []

file_names = [filename.split('.')[0]
              for  filename in os.listdir('/home/jyothish/Downloads/Total_wav_2')
                if filename.endswith('.wav')]


sample_rate, X = scipy.io.wavfile.read('/home/jyothish/Downloads/pop_wav/jazz_ATMA-Jack_s_Song.wav')
#MFCC calculation for test sample
ceps, mspec, spec = mfcc(X[217350:226170])
num_ceps = len(ceps)
X = []
X.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
Vx = np.array(X) # use Vx as input values vector for neural net, k-means, etc

#print("test Vector", Vx[0])
    
with open('/home/jyothish/Downloads/Features/total_features.pickle', 'rb') as handle:
    read = pickle.load(handle)
    
#print(len(read))

sorted_file_names = sorted(file_names)

nnsearch = NearestNeighborSearch()

for i in range(len(read)):
    nnsearch.add_features(read[i])
    
print(nnsearch.featurecount())   

dist_dictionary = nnsearch.apply(query_feature=Vx[0])

distance_list = []
sorted_distance_list = []

for i in range(len(sorted_file_names)):
    #print(sorted_image_names[i])
    #print(dist_dictionary['distances'][sorted_image_names[i]])
    sorted_dist_dictionary = {dist_dictionary['distances'][sorted_file_names[i]] : sorted_file_names[i]}
    distance_list.append(sorted_dist_dictionary)

sorted_distance_list = sorted(distance_list)

print(sorted_distance_list)
