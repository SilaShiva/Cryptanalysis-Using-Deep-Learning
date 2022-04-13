# Cryptanalysis-Using-Deep-Learning

Cryptanalysis identifies weaknesses of ciphers and investigates methods to exploit them in order to compute the plaintext and/or the secret cipher key. Exploitation is nontrivial and, in many cases, weaknesses have been shown to be effective only on reduced versions of the cipher. The goal is to perform Cryptanalysis on Classical Ciphers using Neural Networks.

## Dataset

The dataset was created using the <a href="https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt">Common Passwords List</a> from Kaggle. While this can be done with any NLP Dataset, using this particular dataset gives a twofold advantage:

Passwords can often be random.
Passwords are limited by length, so the computation required is lower.
Passwords are one single word, so sequence dependency will not be a problem.
The dataset is large (14 million passwords) and thus can be cut short to speed up the training process.

## Models
1. LSTM

The network architecture used was a basic LSTM model, with SoftMax, TimeDistrubuted Activation functions. Input is preprocessed for optimal calculation and then fed into the Model. 

2. GRU

The network architecture used was a basic GRU model, with SoftMax, TimeDistrubuted Activation functions. Input is preprocessed for optimal calculation and then fed into the Model. 
