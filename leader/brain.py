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
    def show_data(self,table_name,col1):
        from ..analysis import Select,Data_db

        os.chdir(self.folder)
        
        connection_type=Data_db()
        reader_item=connection_type.table_data(table_name,col1)
        #https://towardsdatascience.com/multi-class-text-classification-with-lstm-1590bee1bd17
        #print("Info",reader_item.info())
        print("reader_item",reader_item[:10])
        print("reader_item[""col1]",reader_item[col1][:10])
 ## split by new lines and spaces
        #reviews_split = all_text.split('\n')
        #all_text = ' '.join(reviews_split)

        ## create a list of words
        #words = all_text.split()

        reader_names=reader_item.col1.value_counts()
        print("______names categories________",reader_names[5])

        reader_id=reader_item.id_inside_cagegory.value_counts()
        print("______id categories________",reader_id)

        #reader_inside_category=reader_item.reader_inside_category.value_counts()
        # encode the text and map each character to an integer and vice versa

        # we create two dictionaries:
            #first deictionaries for id
        chars_id = tuple(set(reader_id))
        int2char = dict(enumerate(chars_id))
        char2int = {ch: ii for ii, ch in int2char.items()}
        
        ## encode the text
        encoded_id = np.array([char2int[ch] for ch in reader_id])
        
        
        #========================================

        print("encoded_id categories",encoded_id)
        #data pre-process for names
        chars_names = tuple(set(reader_names))
        int2char_id = dict(enumerate(chars_id))
        char2int_id = {ch: ii for ii, ch in int2char.items()}
        print("____________ reader_name categories",reader_names)
        ## encode the text
        encoded_names= np.array([char2int[ch] for ch in reader_names])
        print("encoded_name categories",encoded_names)

        
           #second deictionaries for name
        #filter names by id
        #list_id=list(reader_item["id_inside_cagegory"])
        print("reader_id",reader_names.value_counts())
        names=[]
        for id in reader_id.value_counts():
            reader_item_filter=reader_item[reader_item["id_inside_cagegory"]==id]
            names_items=[]
            for i in reader_item_filter.col1:
                col1_items.append(reader_item_filter.col1)
                col1.append(col1_items)
            #return col1
        print(col1,col1)
        writer = pd.ExcelWriter(self.writefile)
        col1_df=pd.DataFrame(col1)
        col1_df.to_excel(writer,"data")
        
        writer.save()

        chars_id = tuple(set(reader_col1))
        int2char_name = dict(enumerate(chars_id))
        char2int_name = {ch: ii for ii, ch in int2char_name.items()}
        
        
        ## encode the text
        encoded_id = np.array([char2int_name[ch] for ch in reader_col1])
        print("encoded_id categories",encoded_id)

        #Pre-processing the data¶
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
