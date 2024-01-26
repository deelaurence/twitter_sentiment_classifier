import tensorflow as tf
import json
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences


from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# import tensorflow as tf
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

new_model = tf.keras.models.load_model('twitter_sentiment_model.keras')


# Show the model architecture
# new_model.summary()

def loadModelAndTokenizer(model_path, tokenizer_path):
    # Load the Keras model
    print(model_path)
    model = load_model(model_path)
    print("here")


    # Load the tokenizer
    with open(tokenizer_path, 'r', encoding='utf-8') as f:
        tokenizer_config = f.read()
        # print((tokenizer_config))

     
        tokenizer=tf.keras.preprocessing.text.tokenizer_from_json(
                tokenizer_config
        )
     # Deserialize the tokenizer config
        # tokenizer = tf.keras.preprocessing.text.Tokenizer.from_config(tf.keras.utils.deserialize_keras_object(tokenizer_config))


    return model, tokenizer

# Example usage
model_path = 'twitter_sentiment_model.keras'
tokenizer_path = 'tokenizer.json'
your_max_sequence_length = 20  # Replace with the actual sequence length expected by your model

# Load the model and tokenizer
model, tokenizer = loadModelAndTokenizer(model_path, tokenizer_path)




# Example sentences
sentences = [
  "i love boys", 
  "i hate girls",
  "with sky skill hub i did not really get value for my money",
  "with sky skill hub i did not really get value for my money I will advise everyone not to make a mistake of buying",
  "You call this a platform? lol",
  "I am a pastor who sleeps in the streets"
]


# Tokenize and pad the sequences
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post', maxlen=your_max_sequence_length)

# Ensure the input shape matches your model's expectations
# (This assumes your model expects input of shape (batch_size, sequence_length))
if padded.shape[1] < your_max_sequence_length:
    padded = pad_sequences(sequences, padding='post', maxlen=your_max_sequence_length)

# Make predictions
predictions = model.predict(padded)

print(f"Padded: {sequences}")
# Display the predictions
for sentence, prediction in zip(sentences, predictions):
    class_labels = ['Negative', 'Neutral', 'Positive']
    max_prob_index = tf.argmax(prediction)
    
    print(f"Sentence: {sentence}")
    print(f"Predicted Class: {class_labels[max_prob_index]}")
    print("----")

