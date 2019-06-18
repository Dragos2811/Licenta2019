'''
Created on May 24, 2019

@author: Dragos
'''
from music21 import converter, instrument, note, chord
import glob
from tqdm import tqdm
import numpy as np
from tensorflow.python.keras.utils import to_categorical
def one_hot_encoded(n,n_vocab,d):
    a = np.zeros(n_vocab,dtype= np.bool_)
    a[n] = d
    return a
def get_notes():
    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    notes = []
    n = ["C","C#","D","E-","E","F","F#","G","G#","A","B-","B"]
    pitchnames = [note.Note(no + str(octave)).nameWithOctave for octave in range(8) for no in n ]
    pitchnames.append("C8")
    n_vocab = len(pitchnames)
    for file in glob.glob("midi_songs/*.mid"):
        midi = converter.parse(file)

        print("Parsing %s" % file)
    
        notes_to_parse = None
    
        try: # file has instrument parts
            s2 = instrument.partitionByInstrument(midi)
            notes_to_parse = s2.parts[0].recurse() 
        except: # file has notes in a flat structure
            notes_to_parse = midi.flat.notes
        for element in notes_to_parse:
            if isinstance(element, note.Note):
                #d = element.duration.quarterLength
                c = [one_hot_encoded(pitchnames.index(element.nameWithOctave), n_vocab,1)]
                notes.append(np.concatenate([c,np.zeros((4,n_vocab),dtype = np.bool_)],axis = 0))
            #elif isinstance(element,  note.Rest):
            #notes.append(one_hot_encoded([], n_vocab))
            elif isinstance(element, chord.Chord):
                #d = element.duration.quarterLength
                c = []
                for i,nota in enumerate(element._notes):
                    if i < 5:
                        c.append(one_hot_encoded(pitchnames.index(nota.nameWithOctave), n_vocab,1))
                    else:
                        break
                if i < 4:
                    notes.append(np.concatenate([c,np.zeros((4-i,n_vocab),dtype = np.bool_)],axis = 0))
    notes = np.array(notes)
    print(notes.shape)
    np.save(open('data/notes.pkl', 'wb'), notes)
    return notes
def generateNote():
    #r este numarul de note simultane
    r = np.random.choice(5,1,p=[0.4,0.3,0.2,0.075,0.025])[0] + 1
    return np.concatenate((np.eye(97,dtype = np.bool_)[np.random.choice(97,r)],np.zeros((5-r,97),dtype = np.bool_)),axis=0)
def prepare_sequences_discriminator(notes):
    """ Prepare the sequences used by the Neural Network """
    sequence_length = 20
    print("preparing sequences")
    batch_size = len(notes) - sequence_length
    '''
    true_sequences = []
    fake_sequences = []
    # create input sequences and the corresponding outputs
    for i in tqdm(range(batch_size)):
        true_sequences.append(notes[i:i + sequence_length])
        fake_sequences.append([generateNote() for _ in range(sequence_length)])
    
    
    print("sequences loaded")
    x = np.concatenate([np.array(true_sequences,dtype=np.bool_),np.array(fake_sequences,dtype=np.bool_)],axis = 0)
    np.save(open('data/x_discriminator.pkl', 'wb'), x)
    '''
    x = np.load(open('data/x.pkl', 'rb'))
    x = np.reshape(x, (x.shape[0],x.shape[1],x.shape[2],x.shape[3],1))
    y = np.zeros(2*batch_size)
    print(x.shape,y.shape)
    y[:batch_size] = 1
    idx = np.random.permutation(2*batch_size)
    return x[idx],y[idx]
def prepare_sequences_generator(notes):
    """ Prepare the sequences used by the Neural Network """
    sequence_length = 19
    print("preparing sequences")
    batch_size = len(notes) - sequence_length
    '''
    true_sequences = []
    fake_sequences = []
    # create input sequences and the corresponding outputs
    for i in tqdm(range(batch_size)):
        true_sequences.append(notes[i:i + sequence_length])
        fake_sequences.append([generateNote() for _ in range(sequence_length)])
    
    
    print("sequences loaded")
    x = np.concatenate([np.array(true_sequences,dtype=np.bool_),np.array(fake_sequences,dtype=np.bool_)],axis = 0)
    np.save(open('data/x_generator.pkl', 'wb'), x)
    '''
    x = np.load(open('data/x_generator.pkl', 'rb'))
    x = np.reshape(x, (x.shape[0],x.shape[1],x.shape[2],x.shape[3],1))
    y = np.zeros(2*batch_size)
    print(x.shape,y.shape)
    y[:batch_size] = 1
    idx = np.random.permutation(2*batch_size)
    return x[idx],y[idx]