# Evaluation of different Machine Learning Algorithms for Music Genre Classification

Getting Started
---------------

This project uses Supervised and Unsupervised Classification Algorithms to evaluate 
the accuracy of classifying a song to a Genre.

Prerequisites
-------------
    scipy
    numpy
    scikits.talkbox
    pydub
    sklearn
  

Procedure followed to prepare the train and test datasets:
----------------------------------------------------------

Step 1: Convert the dataset in MP3 to WAV format.

Step 2: Label the train and test dataset with the respective Genre.

Step 3: Extract the features of train and test dataset using MFCC feature extraction algorithm.

Step 4: Store the extracted features as a Pickle file.

Step 5: Use various Machine Learning Algorithms to compare the Accuracy of Classification.
