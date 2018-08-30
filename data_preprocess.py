import codecs
from exps import *
import numpy as np

class text_decoder(object):
    def __init__(self, text_directory, max_vocab_size):
        with codecs.open(text_directory, encoding='utf-8') as f:
            self.text = f.read()
        self.vocab = set(self.text)
        self.vocab_dict = {}
        
        for word in self.vocab:
            self.vocab_dict[word] = self.text.count(word)
            
        self.vocab_tuple = sorted(self.vocab_dict.items(), key=lambda x: x[1], reverse=True)
        
        if len(self.vocab_tuple) > max_vocab_size:
            self.vocab_tuple = self.vocab_tuple[:MAX_VOCAB_SIZE]
            
        self.vocab_list = [x[0] for x in self.vocab_tuple]
        self.vocab_list.append('')
        
        self.word_to_index_table = {}
        for word in self.vocab_list:
            self.word_to_index_table[word] = self.vocab_list.index(word)
            
        self.index_to_word_table = {value:key for key, value in self.word_to_index_table.items()}        
        
        
    @property
    def vocab_size(self):
        return len(self.vocab_list) + 1
    
    
    def word_to_index(self, word):
        if word in self.vocab_list:
            return self.word_to_index_table[word]
        else:
            return len(self.vocab_list)
    
    
    def index_to_word(self, index):
        if index < len(self.vocab_list):
            return self.index_to_word_table[index]
        elif index == len(self.vocab_list):
            return "<unk>"
        else:
            raise Exception('Unknown index!')
       
    
    def text_to_index(self, texts):
        indexes = []
        for word in texts:
            indexes.append(self.word_to_index(word))
        return np.array(indexes)
        
    def index_to_text(self, indexes):
        texts = []
        for index in indexes:
            texts.append(self.index_to_word(index))
        return ''.join(texts)