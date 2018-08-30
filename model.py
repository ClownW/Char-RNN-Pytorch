import torch
from torch import nn
from torch.autograd import Variable
from exps import *

class RNN(nn.Module):
    def __init__(self, VOCAB_SIZE):
        super(RNN,self).__init__()
        self.embed = nn.Embedding(VOCAB_SIZE , INPUT_SIZE, max_norm = 1)
        if EMBEDDING == False:
            input_size = VOCAB_SIZE
        else:
            input_size = INPUT_SIZE
        self.rnn = nn.LSTM(
            input_size=input_size,
            hidden_size=HIDDEN_SIZE,
            num_layers=NUM_LAYER,
            batch_first=True
        )
        self.dropout = nn.Dropout(DROP_PROB)
        self.l_out = nn.Linear(HIDDEN_SIZE, VOCAB_SIZE)
        self.out = nn.Softmax(dim=-1)


    def forward(self, x, h_state, VOCAB_SIZE, embedding=True):
        if embedding:
            x = self.embed(x)
        else:
            x = Variable(torch.zeros(x.shape[0], x.shape[1], VOCAB_SIZE).scatter_(2, x.data.cpu().unsqueeze(2), 1)).cuda()
        r_out, h_state = self.rnn(x, h_state)
        d_out = self.dropout(r_out)
        d_out_reshaped = d_out.view(-1, d_out.shape[2])
        l_out = self.l_out(d_out_reshaped)
        outs = self.out(l_out).view(-1, x.shape[1], VOCAB_SIZE)
        return outs, h_state