__author__ = "Jyothish James"

import os
import pickle
import random
import scipy.io.wavfile
import numpy as np
from scikits.talkbox.features import mfcc
from sklearn import svm, tree, cluster
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score


rows = []

train = []
test = []

train_label = []
test_label = []

test_predicted = []

file_names = []

file_names = [filename.split('.')[0]
              for filename in os.listdir('/home/jyothish/Downloads/Total_wav_2')
              if filename.endswith('.wav')]

sample_rate, X = scipy.io.wavfile.read('/home/jyothish/Downloads/pop_wav/jazz_ATMA-Jack_s_Song.wav')

# MFCC calculation for test sample
ceps, mspec, spec = mfcc(X[217350:226170])
num_ceps = len(ceps)
X = [np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0)]
Vx = np.array(X)  # use Vx as input values vector for neural net, k-means, etc

with open('/home/jyothish/Downloads/Features/total_features.pickle', 'rb') as handle:
    read = pickle.load(handle)

random.shuffle(read, random.random)

for i in range(741):
    train.append(read[i].values()[0])
    train_label.append(read[i].keys()[0])


for j in range(742, 1059):
    test.append(read[j].values()[0])
    test_label.append(read[j].keys()[0])

print("Ground Truth", len(test_label))

# SUPERVISED LEARNING
# -------------------

# KNN
neighbors = KNeighborsClassifier(n_neighbors=11)
neighbors.fit(train,train_label)

# SVM
clf = svm.SVC(gamma=0.001, C=100)
clf.fit(train, train_label)

# Decision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train, train_label)

# Random Forest
clf = RandomForestClassifier(n_estimators=100)
clf = clf.fit(train, train_label)

# ExtraTrees
clf = ExtraTreesClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
clf = clf.fit(train, train_label)

# Adaboost
clf = AdaBoostClassifier(n_estimators=100)
clf = clf.fit(train, train_label)

# GaussianNaiveBayers
gnb = GaussianNB()
gnb = gnb.fit(train, train_label)

# Cross Validation
scores = cross_val_score(clf, train, train_label,cv=5)
print("Scores", scores)
print("Accuracy", scores.mean())


# UNSUPERVISED LEARNING
# ---------------------

k_means = cluster.KMeans(n_clusters=4)
k_means.fit(train)
print(k_means.labels_)
print(train_label)

for h in range(len(test)):
    # SVM
    test_predicted.append(clf.predict(test[h])[0])
    # KNN
    test_predicted.append(neighbors.predict(test[h])[0])
    # Decision Tree
    test_predicted.append(clf.predict(test[h])[0])
    # Random Forest
    test_predicted.append(clf.predict(test[h])[0])
    # ExtraTrees
    test_predicted.append(clf.predict(test[h])[0])
    # GaussianNaiveBayers
    test_predicted.append(gnb.predict(test[h])[0])
    # Adaboost
    test_predicted.append(clf.predict(test[h])[0])


print("Predicted", len(test_predicted))

print("Confusion Matrix", confusion_matrix(test_label, test_predicted))

ac = accuracy_score(test_predicted, test_label)

print("Accuracy", ac)

tn, fp, fn, tp = confusion_matrix(test_label, test_predicted).ravel()

precision = (float(tp)/float(tp+fp))
recall = (float(tp)/float(tp+fn))
accuracy = (float(tp+tn)/float(len(test)))

print(tn, fp, fn, tp)
print(precision, recall, accuracy)
