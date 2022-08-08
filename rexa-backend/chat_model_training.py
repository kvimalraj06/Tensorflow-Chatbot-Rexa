"""Importing necessary packages"""
import json 
import numpy as np
import pickle
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

"""Loading the json conversation file"""
with open("D:/Vimal/Projects/chatbot_thozhan/thozhan-backend/intents.json") as file:
    data = json.load(file)

""" initializing necessary variables """    
training_sentences = [] # Holds all the training data (which are the sample messages in each intent category)
training_labels = [] # Holds all the tags 
labels = [] # holds unique tags
responses = [] #holds all the responses

for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])
    
labels = list(set(training_labels)) # Unique tags


num_classes = len(labels) # length of unique labels

"""Encoding the labels"""

label_encoder = LabelEncoder()
label_encoder.fit(training_labels)
training_labels = label_encoder.transform(training_labels) # Encoded labels


"""vectorizing or pre processing our text data"""

vocab_size = 1000
embedding_dim = 16
max_len = 20
oov_token = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences) # converts text to sequence of numbers
padded_sequences = pad_sequences(sequences, truncating='post', maxlen=max_len) #To make all the training text sequences into the same size


"""Defining model architechture with Sequential” model class of Keras"""
model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(GlobalAveragePooling1D())
model.add(Dense(16, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', 
              optimizer='adam', metrics=['accuracy'])


"""Training our model with training data and labels"""
epochs = 1000
history = model.fit(padded_sequences, np.array(training_labels), epochs=epochs)


"""Saving trained model"""
model.save("D:/Vimal/Projects/chatbot_thozhan/thozhan-backend/chat_model.model")

with open('D:/Vimal/Projects/chatbot_thozhan/thozhan-backend/tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('D:/Vimal/Projects/chatbot_thozhan/thozhan-backend/label_encoder.pickle', 'wb') as ecn_file:
    pickle.dump(label_encoder, ecn_file, protocol=pickle.HIGHEST_PROTOCOL)

