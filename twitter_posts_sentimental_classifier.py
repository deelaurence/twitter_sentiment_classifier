# -*- coding: utf-8 -*-
"""Twitter posts sentimental classifier

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gUnJ3YO7beP8VYY6zGvkLoMCn1-PvFpG
"""

import sys
print("Python Version:", sys.version)
import tensorflow as tf
print("TensorFlow Version:", tf.__version__)

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import json



with open("train_modified.json",'r') as f:
  datastore = json.load(f)


sentences = []
labels = []


for item in datastore:
  sentences.append(item['text'])
  labels.append(item['sentiment'])

part_sentence=sentences[2:5]


tokenizer = Tokenizer(oov_token='<OOV>')

print(part_sentence)

import math
training_size=math.ceil(0.8*len(sentences))
print(training_size)


training_sentences = sentences[0:training_size]
testing_sentences = sentences[training_size:]
testing_labels = labels[training_size:]
training_labels = labels[0:training_size]

tokenizer.fit_on_texts(training_sentences)
word_index=tokenizer.word_index

training_sequences = tokenizer.texts_to_sequences(training_sentences)
training_padded = pad_sequences(training_sequences, padding='post')

testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequences, padding='post')


vocab_size = len(tokenizer.word_index) + 1

# model=tf.keras.Sequential([
#     tf.keras.layers.Embedding(input_dim=vocab_size,output_dim=20),
#     tf.keras.layers.GlobalAveragePooling1D(),
#     tf.keras.layers.Dense(24, activation='relu'),
#     tf.keras.layers.Dense(1, activation='sigmoid')
# ])

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

num_epochs=30

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=20),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')  # Use 'softmax' for multi-class classification
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


import numpy as np
training_labels = np.array(training_labels)
training_padded = np.array(training_padded)
testing_labels = np.array(testing_labels)
testing_padded = np.array(testing_padded)

history= model.fit(training_padded, training_labels, epochs=num_epochs,
                   validation_data=(testing_padded, testing_labels))

model.save('twitter_sentiment_model.keras')



sentence=[
    "I am a pastor right, but i still choose to clean the streets",
    "i am a carpenter"
]



sequences= tokenizer.texts_to_sequences(sentence)

padded= pad_sequences(sequences,padding='post')
print(padded)
print(model.predict(padded))