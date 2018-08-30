INPUT_SIZE = 128                   #the 3rd dimension of input
TIME_STEP = 80                     #time_step of rnn
MAX_VOCAB_SIZE = 5500              #size of the vocabulary
HIDDEN_SIZE = 1024                 #hidden_size of rnn
NUM_LAYER = 3                      #number of layers of rnn
BATCH_SIZE = 32                    #number of sequences in one batch
EPOCH = 1000                       #number of training epoch
LR = 0.001                         #learning rate
DROP_PROB = 0                      #the drop_prob in drop_out layer
SPLIT_PROB = 0.1                   #the prob for spliting training and dev set
START_WORD_LENGTH = 8              #the length of start word when sample(must be larger than 0)
SAMPLE_LENGTH = 500                #the length of the sample text
N_SAMPLE = 5                       #the top n prob to be sampled when sampling

EMBEDDING = True
filename = "./data/novel.txt"      #the directory of the text file