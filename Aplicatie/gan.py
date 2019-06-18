'''
Created on May 27, 2019

@author: Dragos
'''



import numpy as np

from tensorflow.python.keras.models import Sequential,Model
from tensorflow.python.keras.layers import ConvLSTM2D,BatchNormalization,Conv3D,concatenate
from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.layers import Input
from utils import get_notes,prepare_sequences_generator
from discriminator import discriminator


def generator():
    """ create the structure of the neural network """
    seq = Sequential()
    seq.add(ConvLSTM2D(filters=40, kernel_size=(3, 3),
                       input_shape=(19, 5, 97, 1),
                       padding='same', return_sequences=True))
    seq.add(BatchNormalization())
    
    seq.add(ConvLSTM2D(filters=40, kernel_size=(3, 3),
                       padding='same', return_sequences=True))
    seq.add(BatchNormalization())
    
    seq.add(ConvLSTM2D(filters=40, kernel_size=(3, 3),
                       padding='same', return_sequences=True))
    seq.add(BatchNormalization())
    
    seq.add(ConvLSTM2D(filters=40, kernel_size=(3, 3),
                       padding='same', return_sequences=True))
    seq.add(BatchNormalization())
    
    seq.add(Conv3D(filters=1, kernel_size=(19, 1, 1),
                   activation='sigmoid'))
    seq.compile(loss='binary_crossentropy',
                optimizer='adadelta')
    return seq

    
def gan(D,G):
    D.trainable = False
    D.load_weights('weights/discriminator-01-0.0114-0.9961.hdf5')
    gan_input = Input(shape=(19,5,97,1))
    prediction = G(gan_input)
    x = concatenate([gan_input,prediction],axis = 1)
    gan_output = D(x)
    gan = Model(inputs= gan_input,outputs=gan_output)
    gan.summary()
    gan.compile(loss='binary_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
    return gan
def train_gan():
    notes = np.load(open('data/notes.pkl', 'rb')) 
    #notes = get_notes()
    x,y = prepare_sequences_generator(notes)
    model = gan(discriminator(),generator())
    
    filepath = "weights/discriminator-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(
        filepath,
        monitor='loss',
        verbose=0,
        save_best_only=True,
        mode='min'
    )
    callbacks_list = [checkpoint]

    model.fit(x,y,validation_split=0.3, epochs=200, batch_size=32, callbacks=callbacks_list)
if __name__ == '__main__':
    train_gan()
    
    
    