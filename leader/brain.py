'''
this model based on Character-Level LSTM in PyTorch form udacity
recurrent-neural-networks/char-rnn
we also use word2vec-embeddings 
'''
#from .network import Model
#from .train import Train

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from .network import TextRnn as Model
from .train import TexTrainer
import torch
from torch import nn
import torch.nn.functional as F
#from local library
from .utiliy import get_batches
#Load and prepare the data
class Thinking():    
    def __init__(self,folder,output):
        self.show_data
        self.folder=folder
        self.output=output
    def show_data(self,schema,table_name,*args,word=True,sentince=True):
        from ..analysis import Select,Data_db
        #self.show_data.__init__(self, list(args))
        os.chdir(self.folder)
        
        connection_type=Data_db()
        reader_item=connection_type.table_data(schema,table_name,*args)
        #https://towardsdatascience.com/multi-class-text-classification-with-lstm-1590bee1bd17
        #print("Info",reader_item.info())
        print("reader_item",reader_item[:10])
        col1=0
        col=list(args)
        col=col[col1]
        cols=col.split(",")
        
        col_name=cols[0]
        col_id=cols[1]


        counts_names=reader_item[col_name].value_counts()
        print("______names categories________",counts_names[5])

        counts_id=reader_item[col_id].value_counts()
        print("______id categories________",counts_id)
        print("reader_item col_name",col_name,reader_item[col_name])
        #reader_inside_category=reader_item.reader_inside_category.value_counts()
        # encode the text and map each character to an integer and vice versa

        if word:
            # we create two dictionaries:
                    #data pre-process for names
            chars_names = tuple(set(counts_names))
            int2char_name = dict(enumerate(counts_names))
            char2int_name = {ch: ii for ii, ch in int2char_name.items()}
            encoded_names= np.array([int2char_name[ch] for ch in counts_names])
            #========================================
                #first deictionaries for id
            chars_id = tuple(set(counts_id))
            int2char = dict(enumerate(chars_id))
            char2int = {ch: ii for ii, ch in int2char.items()}
            
            ## encode the text
            encoded_id = np.array([char2int[ch] for ch in counts_id])
            
        if sentince:
            #transfere dataframe to list
            # معايير تحديد الجمل الاسمية والفعلية            
            tow_words=reader_item.split("و")
            print("test___________ tow_words",tow_words.head(5))
            #data pre-process for names
            chars_names = tuple(set(counts_names))
            int2char_name = dict(enumerate(counts_names))
            char2int_name = {ch: ii for ii, ch in int2char_name.items()}
            encoded_names= np.array([int2char_name[ch] for ch in counts_names])
            #========================================
            # create id
                #first deictionaries for id
            chars_id = tuple(set(counts_id))
            int2char = dict(enumerate(chars_id))
            char2int = {ch: ii for ii, ch in int2char.items()}
            
            ## encode the text
            encoded_id = np.array([char2int[ch] for ch in counts_id])        
        print("encoded_id categories",encoded_id)

        print("____________ char2int_name ",char2int_name)
        ## encode the text

        print("encoded_name categories",encoded_names)

        def one_hot_encode(self,arr, n_labels):
            '''
            LSTM expects an input that is one-hot encoded_id meaning that each character 
            is converted into an integer (via our created dictionary) 
            and then converted into a column vector where only it's corresponding integer index will have the value of 1 and the rest of the vector will be filled with 0's. Since we're one-hot encoding the data
            '''
            # Initialize the the encoded_id array
            one_hot = np.zeros((np.multiply(*arr.shape), n_labels), dtype=np.float32)
            
            # Fill the appropriate elements with ones
            one_hot[np.arange(one_hot.shape[0]), arr.flatten()] = 1.
            
            # Finally reshape it to get back to the original array
            one_hot = one_hot.reshape((*arr.shape, n_labels))
            
            return one_hot
        # check that the function works as expected
        test_seq = np.array([[3, 5, 1]])
        one_hot = one_hot_encode(self,test_seq, 8)

        print("____one_hot____",one_hot)
        
        self.batches = get_batches(encoded_id, 8, 50)
        print("____fast test_____ counts_id.self.batches()",self.batches)
        self.x, self.y = next(self.batches)
        # printing out the first 10 items in a sequence
        print('x\n', self.x[:10, :10])
        print('\ny\n', self.y[:10, :10])

        self.batches_name = get_batches(encoded_col1, 8, 50)
        self.z, self.t = next(self.batches_name)
        # printing out the first 10 items in a sequence
        print('z\n', self.z[:10, :10])
        print('\ny\n', self.t[:10, :10])
        # check if GPU is available
        train_on_gpu = torch.cuda.is_available()
        if(train_on_gpu):
            print('Training on GPU!')
        else: 
            print('No GPU available, training on CPU; consider making n_epochs very small.')
        ## : set you model hyperparameters
        # define and print the net
        n_hidden=512
        n_layers=2

        #net = Model(chars_col1, n_hidden, n_layers)
        net = Model(chars_id, n_hidden, n_layers)
        print(net)
        batch_size = 128
        seq_length = 100
        n_epochs =  20 # start small if you are just testing initial behavior

        # train the model
        #TexTrainer(net, encoded_col1, epochs=n_epochs, batch_size=batch_size, seq_length=seq_length, lr=0.001, print_every=10)
        TexTrainer.train(net, encoded_id, epochs=n_epochs, batch_size=batch_size, seq_length=seq_length, lr=0.001, print_every=10)

        ## change the name, for saving multiple files

        model_name = 'rnn_x_epoch.net'

        checkpoint = {'n_hidden': net.n_hidden,
                    'n_layers': net.n_layers,
                    'state_dict': net.state_dict(),
                    'tokens': net.chars}

        with open(model_name, 'wb') as f:
            torch.save(checkpoint, f)
        # change the name, for saving multiple files
        
        model_name = 'rnn_x_epoch.net'

        checkpoint = {'n_hidden': net.n_hidden,
                    'n_layers': net.n_layers,
                    'state_dict': net.state_dict(),
                    'tokens': net.chars}

        with open(model_name, 'wb') as f:
            torch.save(checkpoint, f)
