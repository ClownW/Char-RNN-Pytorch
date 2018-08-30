import torch
from torch import nn
from torch.autograd import Variable
import numpy as np
import codecs
from data_preprocess import text_decoder
from exps import *

max_step = SAMPLE_LENGTH
n_sample = N_SAMPLE

decoder = text_decoder(filename, MAX_VOCAB_SIZE)
rnn = torch.load('./pkl/novel/rnn_novel_final.pkl').eval()

#sample word according to their prob
def top_n_sample(prob_tensor, n=5):
    top_n = torch.topk(prob_tensor.data, n, dim=-1)
    prob_index = torch.multinomial(top_n[0].squeeze(), num_samples=1)
    lst = []
    for i in range(top_n[1].shape[1]):
        lst.append(int(top_n[1][:,i,int(prob_index[i])].cpu().numpy()))
    return lst

#the words you hope to start the text, the length of start_words is the step of rnn when sample
start_words = " "*START_WORD_LENGTH
index = Variable(torch.LongTensor(decoder.text_to_index(start_words)).unsqueeze(0)).cuda()
text = start_words
h_state = None

for i in range(max_step):
    temp = Variable(torch.zeros(index.shape).long()).cuda()
    prob, _ = rnn(index, h_state, decoder.vocab_size, embedding=EMBEDDING)
    pred_word = top_n_sample(prob, n=n_sample)
    word = decoder.index_to_text(pred_word)
    if word != '':
        text += word[-1]
    if index.shape[1] > 1:
        temp[:,:-1], temp[:,-1]= index[:,1:], Variable(torch.LongTensor([pred_word[-1]])).unsqueeze(0).cuda()
    elif index.shape[1] == 1:
        temp = Variable(torch.LongTensor([pred_word[-1]])).unsqueeze(0).cuda()
    else:
        raise Exception('index shape error!')
    index = temp
    
print(text)
