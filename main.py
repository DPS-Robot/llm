from llamaapi import LlamaAPI
from dotenv import load_dotenv
load_dotenv()
import os
import json
import pyfirmata
llama = LlamaAPI(os.getenv("API_KEY"))
from speech import record_audio, transcribe
from speechSynthesis import gen

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
    "model": "phi3:mini",
    "messages": [
        {
            "role": "user",
            "content": "ALWAYS RESPOND BRIEFLY AND IN 1 SENTENCE, NEVER USE MORE THAN 1 SENTENCE. ALL NUMBERS YOU HAVE TO SPELL OUT. DO NOT RESPOND ANYTHING ELSE. ONLY THAT 1 SENTENCE"
        }
    ],
    "stream": False
}

data2 = {
    "model": "phi3:mini",
    "messages": [
        {
            "role": "user",
            "content": "tell it to do functions here"
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

def functions(q):
    url = "http://localhost:11434/api/chat"
    data["messages"].append({"role": "user", "content": q})
    response = requests.post(url, json=data)
    response = response.json()
    return response["message"]["content"]

def facialExpression(emotion):
    print(f"Facial Expression Function Working, Parameter Recieved is {emotion}")

while True:
    prompt = transcribe(record_audio())
    print("Audio Processed \n\n")
    print(f"You: {prompt}")
    output = ask(prompt)
    #func = functions(prompt)
    print(f"Bot: {output}")
    gen(output)
    #playAudio()
    #api_request_json["messages"].append({"role": "user", "content": prompt})
    #response = llama.run(api_request_json)
    #responseArray = json.dumps(response.json()["choices"][0]["message"]["content"]).replace('"', '').split("$")
    #print(responseArray[0])
    #api_request_json["messages"].append({"role": "system", "content": responseArray[0]})
    #array = responseArray[1].replace(" ", "").split(',')


    # Make the LLM Send it separated by commas then split that thing at commas and push to array
    """
    for i in array:
        try:
            eval(i)
        except:
            print("Error in function")

            """