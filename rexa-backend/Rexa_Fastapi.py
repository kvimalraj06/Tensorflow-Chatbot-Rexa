"""Importing necessary packages"""
import json
from django.http import response 
import numpy as np
from tensorflow import keras
import pickle
import time
time.clock = time.time
from services import words_handler, store_query
from controllers import save_chat, fetch_user_specific
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

"""Starting FastAPI"""
app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""loading the model for general queries"""

chat_model = keras.models.load_model('chat_model.model')
# load tokenizer object
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load label encoder object
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

with open("intents.json") as file:
    data = json.load(file)

max_len = 20

"""Route API"""
@app.get("/")
async def read_root():
    return {"Rexa": "Welcome to Rexa"}


"""Bot Reply"""
@app.get("/msg")
async def read_item(query: Union[str, None] = None):
    input = query
    meaningful = words_handler.meaningful_check(input)
    details = fetch_user_specific.fetch_details("vimal")

    if meaningful:
        result = chat_model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([input]),
                                            truncating='post', maxlen=max_len))

        tag = lbl_encoder.inverse_transform([np.argmax(result)])#converting the sequence into tag

        for intent in data['intents']:
            if intent['tag'] == tag:
                if intent['context_action']:
                    detail_header = np.random.choice(intent['responses'])
                    if detail_header in details:
                        return {"bot_response":details[detail_header],"input_chat":input}
                    else:
                        return {"bot_response":"Detail not found","input_chat":input}
                else:
                    bot_response = np.random.choice(intent['responses']) # pick any one response under the matched tag

        if tag == "Default":
            save_chat.save(input,bot_response)
            store_query.save(input)
            return {"bot_response":bot_response, "input_chat":input}
        else:
            save_chat.save(input,bot_response)
            return {"bot_response":bot_response, "input_chat":input}
    else:
        return{"bot_response":"I can't understand", "input_chat":input} # Handle meaningless(naughty) words
