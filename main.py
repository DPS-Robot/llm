from llamaapi import LlamaAPI
from dotenv import load_dotenv
load_dotenv()
import os
import json
import pyfirmata
llama = LlamaAPI(os.getenv("API_KEY"))
from speech import record_audio, transcribe

import speech_recognition as sr
import requests
 
r = sr.Recognizer()
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening")
            aud = r.listen(source)
            print("Processing")
            txt = r.recognize_google(aud)
            txt = txt.lower()
            return txt
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "Errorred"
         
    except sr.UnknownValueError:
        print("unknown error occurred")
        return "Errorred"

"""
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

model_id = "vikhyatk/moondream2"
revision = "2024-05-20"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

image = Image.open('sample.jpg')
enc_image = model.encode_image(image)
description = model.answer_question(enc_image, "Describe this image.", tokenizer)
"""
description = "Black"



def rightArm(deg):
    print(f"rightArm() Function Working, Parameter Recieved is {deg}")

def leftArm(deg):
    print(f"leftArm() Function Working, Parameter Recieved is {deg}")

happy = "happy"
sad = "sad"
angry = "angry"
neutral = "neutral"
surprised = "surprised"
disgusted = "disgusted"
scared = "scared"
laughing = "laughing"
crying = "crying"

data = {
    "model": "tinyllama",
    "messages": [
        {
            "role": "user",
            "content": "YOU WILL ONLY ALWAYS RESPOND BRIEFLY, ONLY BETWEEN 1 TO 20 WORDS."
        }
    ],
    "stream": False
}

def ask(q):
    url = "http://localhost:11434/api/chat"
    data["messages"].append({"role": "user", "content": q})
    response = requests.post(url, json=data)
    response = response.json()
    return response["message"]["content"]

def facialExpression(emotion):
    print(f"Facial Expression Function Working, Parameter Recieved is {emotion}")

while True:
    prompt = listen()
    print("Audio Processed \n\n")
    print(f"You: {prompt}")
    print(ask(prompt))
    #api_request_json["messages"].append({"role": "user", "content": prompt})
    #response = llama.run(api_request_json)
    #responseArray = json.dumps(response.json()["choices"][0]["message"]["content"]).replace('"', '').split("$")
    #print(responseArray[0])
    #api_request_json["messages"].append({"role": "system", "content": responseArray[0]})
    #array = responseArray[1].replace(" ", "").split(',')
    #for i in array:
    #    try:
    #        eval(i)
    #    except:
    #        print("Error in function")