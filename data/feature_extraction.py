__author__ = "Jyothish James"

import scipy.io.wavfile
import numpy as np
from scikits.talkbox.features import mfcc
import os
import pickle

file_names = []
feature_dict = []

file_names = [filename.split('.')[0]
              for filename in os.listdir('/home/jyothish/Downloads/rock_wav')
              if filename.endswith('.wav')]

for i in range(len(file_names)):  # Here X is not normalized
    sample_rate, X = scipy.io.wavfile.read('/home/jyothish/Downloads/rock_wav/' + file_names[i] + '.wav')

    # MFCC calculation
    ceps, mspec, spec = mfcc(X[224910:260190])
    num_ceps = len(ceps)
    X = [np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0)]
    Vx = np.array(X)  # use Vx as input values vector for neural net, k-means, etc
    label = "rock"

    # Storing to Dictionary
    dictionary = {label: Vx[0]}
    feature_dict.append(dictionary)  # Storing the features as dictionary

# Write as pickle file
with open('/home/jyothish/Downloads/Features/rock_features.pickle', 'wb') as handle:
    pickle.dump(feature_dict, handle)
print(len(feature_dict))
print(feature_dict)
