# Char-RNN-Pytorch
Char-RNN building by Pytorch for generating Chinese text

一个基于Pytorch来实现的char-rnn，用来产生中文文本，可以生成小说和作文。

详细介绍见博客：https://cloud.tencent.com/developer/article/1199264

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

## Result

以小说《斗破苍穹》为训练集时的采样结果：

```
         之内有着一个极为微小的冰落，一时间，只见得一道能量涟截扩散而开，只见得那地方，便是有着不少势力稍弱的强者会自爆，这种魔兽，实在是出人意料，难道这便是我第一次来到这里，所为的，便是能够轻复将之得罪，也不用太过据心……
    “待！”
    望着那被萧炎握住脖诺心尖与那火毒爆裂而开的龙力丹，顿时，一钱漆黑的凭体，顿时，一股雪白的能量涟截暴涌而出，让得人心头寒意。
    “这些该死的魔炎谷，革是此
```

用小学生作文为训练集时的采样结果：

```
                    走，夏天听到了！
     还带一年晚的时光里，我们只看了看，仿佛在说：“我终于来到我了！”
    我们找了一条小本，我穿着长长的河水，掩出土地点点头，有点像小摆一样，不然，我溜车起来。有事老爷爷给我踩了一大块的纸片。每到冲天，到了秋天的丰收，和庐去给大地母亲的线抱，大自然也会鼓鼓无动。
             ——题记
空歌想就知道这些都是为了自己的做好事而又有一种力。
 
```

```
                         没有钱，我便在那边，我一边听，边说边走开，把我送到沙滩。我拿着瓶子，跑到了小黄鼠的身后，大声得对小草说：“你们真是不可思灭呀！不会这么做，就一个小小的举世中，我们不能与同学打架，但那比太阳、云去的雪白的阳光照在我心里。我有着心灵的感觉，仿佛是是在寻找下面要怎么办？怎么办？这下凤了！
    可是，老师不吸为什么老师而不对我们继续说的，

          我的妈妈是一个伟大的母爱。
```

