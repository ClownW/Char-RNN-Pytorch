import torch
from torch import nn
from torch.autograd import Variable
import numpy as np
import time
import os
from data_preprocess import text_decoder
from model import RNN
from exps import *
import matplotlib.pyplot as plt


#prepare the input data for rnn
decoder = text_decoder(filename, MAX_VOCAB_SIZE)
word_indexes = decoder.text_to_index(decoder.text)
n_batches = int(len(word_indexes)/(BATCH_SIZE*TIME_STEP))
word_indexes = word_indexes[:n_batches*BATCH_SIZE*TIME_STEP]
input_indexes = word_indexes.reshape((n_batches, BATCH_SIZE, TIME_STEP))

input_indexes_train, input_indexes_dev = input_indexes[:-int(input_indexes.shape[0]*SPLIT_PROB)],input_indexes[-int(input_indexes.shape[0]*SPLIT_PROB):]

#build the rnn and optimizer
rnn = RNN(decoder.vocab_size).cuda()
optimizer = torch.optim.Adam(rnn.parameters(), lr=LR)
#learning rate decay for training
scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=[100,200,300,400,600,750,850,930])
loss_func = nn.NLLLoss()


h_state = None
loss_lst = []

for epoch in range(EPOCH):
    scheduler.step()
    np.random.shuffle(input_indexes)
    for batch in range(input_indexes.shape[0]):
        start = time.time()
        #prepare x, y
        x = Variable(torch.LongTensor(input_indexes[batch, :, :])).cuda()
        y = torch.from_numpy(np.zeros((x.shape))).cuda()
        y[:, :-1] , y[:, -1] = x[:,1:].data, x[:, 0].data
        
        #for printing the results when training
        x_temp = input_indexes[batch, :, :]
        y_temp = y.cpu().numpy()
        
        prediction, h_state = rnn(x, h_state, decoder.vocab_size, embedding=EMBEDDING)
        #unpacking and packing h_state, cuda will report error if not do that
        h_state0 = Variable(h_state[0].data, requires_grad=True)
        h_state1 = Variable(h_state[1].data, requires_grad=True)
        h_state = tuple([h_state0, h_state1])
        
        #for calculating the NLLLoss,add an additional 1e-20 to avoid gradient exploding
        pred = torch.log(prediction.view(-1, decoder.vocab_size) + 1e-20)    
        target = Variable(y.view(-1))

        loss = loss_func(pred, target.long())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        end = time.time()
        #print some info every 200 batches
        if batch % 200 == 0:
            print("Epoch: {}".format(epoch), 
                  "| Batch: {}".format(batch), 
                  "| loss: {:.4f}".format(loss.data.cpu().numpy()[0]), 
                  "| time spent: {:.4f}".format((end - start)))
    #save model every 100 epoches
    if epoch % 100 == 1:
        if not os.path.exists("./new_trained"):
            os.makedirs("./new_trained")
        directory = './new_trained/rnn_novel'+str(epoch)+'.pkl'
        torch.save(rnn, directory)
    
    #print the output word every epoch to see how the model performs        
    pred_word = torch.max(prediction,2)[1].data.cpu().numpy()
    print('\n'*2, "Epoch: {}".format(epoch))
    print('\n', "input:", decoder.index_to_text(x_temp[0]))
    print('\n', "expected output:", decoder.index_to_text(y_temp[0]))
    print('\n', "output:", decoder.index_to_text(pred_word[0]))
    
    #this is the cross-validation part
    if epoch % 2 == 0:
        rnn.eval()
        n = np.random.randint(0,input_indexes_dev.shape[0])
        h_state1 = None
        x_dev = Variable(torch.LongTensor(input_indexes_dev[n, :, :])).cuda()
        y_dev = torch.from_numpy(np.zeros((x_dev.shape))).cuda()
        y_dev[:, :-1] , y_dev[:, -1] = x_dev[:,1:].data, x_dev[:, 0].data
        
        x_temp1 = input_indexes_dev[n,:,:]
        y_temp1 = y_dev.cpu().numpy()
        
        
        prediction1, h_state1 = rnn(x_dev, h_state1, decoder.vocab_size, embedding=EMBEDDING)
        pred1 = torch.log(prediction1.view(-1, decoder.vocab_size) + 1e-20) 
        target1 = Variable(y_dev.view(-1))
        pred_word1 = torch.max(prediction1,2)[1].data.cpu().numpy()
        loss1 = loss_func(pred1, target1.long())
        print('-'*80)
        print("below is the dev part")
        #by comparing the loss with training set to see whether overfit or not
        print('\n'*2, "Epoch: {}".format(epoch), "| loss1: {:.4f}".format(loss1.data.cpu().numpy()[0]))
        print('\n', "x_dev:", decoder.index_to_text(x_temp1[0]))
        print('\n', "expected output:", decoder.index_to_text(y_temp1[0]))
        print('\n', "output:", decoder.index_to_text(pred_word1[0]))
        print('\n', "above is the dev part")
        print('-'*80)
        rnn.train() 
    
    loss_lst.append(loss.data.cpu().numpy())

plt.plot(loss_lst)
plt.show()
