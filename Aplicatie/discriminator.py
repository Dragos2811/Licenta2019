'''
Created on May 5, 2019

@author: Dragos
'''
from tensorflow.python.keras.layers import Conv3D,MaxPooling3D,Dropout,LeakyReLU,Dense,Flatten
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.callbacks import ModelCheckpoint
from tensorflow.python.keras.optimizer_v2.rmsprop import RMSProp
import numpy as np
from utils import prepare_sequences_discriminator,get_notes
def discriminator():
    model = Sequential()
    model.add(Conv3D(64,(3,3,3),
                     activation = 'relu',
                     padding="same",
                     input_shape =(20,5,97,1)))
    model.add(MaxPooling3D((2,2,2)))
    model.add(Conv3D(128,(3,3,3),
                     activation = 'relu',
                     padding="same"))
    model.add(MaxPooling3D((2,2,2)))
    model.add(Conv3D(512,(3,3,3),
                     activation = 'relu',
                     padding="same"))
    model.add(Dropout(0.2))
    model.add(Conv3D(1024,(3,3,3),
                     activation = 'relu',
                     padding="same"))
    model.add(LeakyReLU(0.2))
    model.add(Flatten())
    model.add(Dense(1,activation='sigmoid'))
    model.compile(loss='binary_crossentropy',
                   optimizer=RMSProp(),
                   metrics=['acc'])
    return model

def train_discriminator():
    notes = np.load(open('data/notes.pkl', 'rb')) 
    #notes = get_notes()
    print("Notes loaded")
    x,y = prepare_sequences_discriminator(notes)
    print("Sequences loaded",x.shape,y.shape)
    model = discriminator()
    
    filepath = "weights/discriminator-{epoch:02d}-{loss:.4f}-{acc:.4f}.hdf5"
    checkpoint = ModelCheckpoint(
        filepath,
        monitor='loss',
        verbose=0,
        save_best_only=True,
        mode='min'
    )
    callbacks_list = [checkpoint]

    model.fit(x,y,validation_split=0.3, epochs=1, batch_size=32, callbacks=callbacks_list)
    model.save_weights('weights/discriminator-01-0.0114-0.9961.hdf5')
if __name__ == '__main__':
    train_discriminator()
    #D = discriminator()
    #d.load_weights()