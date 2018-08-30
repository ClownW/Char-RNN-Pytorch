# Char-RNN-Pytorch
Char-RNN building by Pytorch to generating Chinese text

一个基于Pytorch来实现的char-rnn，用来产生中文文本，可以生成小说和作文。

## Requirements
* python 3.5
* Pytorch 0.3.X
* CUDA

## Instruction
1. data_preprocess.py is used for generating the vocabulary, converting texts to indexes or indexes to texts
2. exps.py lists hyperparameters for this project
3. model.py includes the RNN model built by Pytorch
4. train.py is used for training the model, printing the output texts every epoch for training set and every two epochs for dev set
5. sample.py is used for generating texts using the trained model, since the saved pkl file is to large to upload, you need to train the model youself and change the directory for loading your model when sampling

aaaaaa