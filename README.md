# Char-RNN-Pytorch
Char-RNN building by Pytorch to generating Chinese text

一个基于Pytorch来实现的char-rnn，用来产生中文文本，可以生成小说和作文。

## Requirements
* python 3.5
* Pytorch 0.3.X
* CUDA

## Instruction
1. data_preprocess.py is used for generating the vocabulary, converting texts to indexes or indexes to texts

   data_preprocess.py用来产生词汇表，将文本转换成索引以及将索引转换成文本

2. exps.py lists hyperparameters for this project including the filename of the training data. Training data is not provided here to avoid the infringement of copyright.However, crawler scripts were uploaded for

   crawling data.

   exps.py列出了项目中的超参数，包括训练使用的filename等都包含在里面，为避免版权问题这里不直接提供训练数据，但上传了爬虫脚本以供爬取数据。

3. model.py includes the RNN model built by Pytorch

   model.py用Pytorch搭建了RNN模型

4. train.py is used for training the model, printing the output texts every epoch for training set and every two epochs for dev set

   train.py 是用来训练模型，在训练的过程中，每个epoch打印出训练集中输出的文字，每两个epoch中打印出测试集中输出的文字用来进行对比是否过拟合（主要是对比loss）

5. sample.py is used for generating texts using the trained model, since the saved pkl file is to large to upload, you need to train the model youself and change the directory for loading your model when sampling

   sample.py利用训练好的模型来进行采样得到文本。由于训练好的模型pkl文件过大无法上传，只能重新训练模型，并且在采样时修改这个文件中的路径。

6. crawler files are used for crawling for data from the internet. The data is used for training the RNN to generating essays.

   crawler里面包含了两个爬虫文件，爬取了18M的小学生作文作为训练数据。（为避免版权问题这里不直接提供爬取好的文本文件，运行两个爬虫脚本即可下载语料库）
