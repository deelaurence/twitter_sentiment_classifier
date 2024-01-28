
from django.shortcuts import render
import tensorflow as tf
import json
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences


from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


# Create your views here.
# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.utils import load_model_and_tokenizer

model, tokenizer = load_model_and_tokenizer('myapp/twitter_sentiment_model.keras', "myapp/tokenizer.json")

@api_view(['POST'])
def predict_sentiment(request):
    data = request.data
    sentences = data.get('sentences', [])

    # Tokenize and pad the sequences
    sequences = tokenizer.texts_to_sequences(sentences)
    padded = pad_sequences(sequences, padding='post', maxlen=20)

    # Make predictions
    predictions = model.predict(padded)

    # Format predictions
    results = []
    class_labels = ['Negative', 'Neutral', 'Positive']
    for sentence, prediction in zip(sentences, predictions):
        max_prob_index = tf.argmax(prediction)
        result = {"sentence": sentence, "predicted_class": class_labels[max_prob_index]}
        results.append(result)

    return Response({"predictions": results})

