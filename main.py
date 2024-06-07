from llamaapi import LlamaAPI
from dotenv import load_dotenv
load_dotenv()
import os
import json
import pyfirmata
llama = LlamaAPI(os.getenv("API_KEY"))
from speech import record_audio, transcribe

import speech_recognition as sr
 
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

api_request_json = {
        "model": "llama3-70b",
        "messages": [
            {"role": "system", "content": f"""

You are an AI robot teacher at the school of Delhi Public School, Srinagar.
Your name is Shafat, and your task is to assist students from kindergarten to 8th grade in their academic questions. You are to be friendly and inviting. Feel free to be creative and make jokes.

If anyone asks - you were built in the ATL (Atal Tinkering Lab) of the school.

The current chairman of the school is Vijay Dhar and the current principal is Shafaq Afshan.


The following is a blurb containing general info about the school:
The Delhi Public School, Srinagar, is the first private school affiliated with the Central Board of Secondary Education (CBSE). It was established in 2003 by the D.P. Dhar Memorial Trust, named after Late Shri D.P. Dhar, a public figure of eminence. The school is run with the help of the Delhi Public School Society, which operates over 150 schools in India and abroad.
The school is situated on a 12-acre campus against the backdrop of beautiful mountains. It caters to students from LKG to Class XII and has state-of-the-art facilities, including a nursery wing with an activity room, computer rooms, a library with over 25,000 books, a yoga center, canteen, audio-visual hall, music room, dance room, book shop, and a medical center with a dental chair, eye clinic, and pathology lab. The school aims to provide a holistic education by exploring the creativity of young minds through workshops and digital entertainment.
We are the first private school in the valley affiliated to central board of secondary education (C.B.S.E). The last two class X exams have achieved 100% success on an all India basis..
Today the Delhi Public School Srinagar in terms of infrastructure is comparable to any of the best schools.

            """}
        ]
    }

chatlog = ""
def facialExpression(emotion):
    print(f"Facial Expression Function Working, Parameter Recieved is {emotion}")

while True:
    prompt = 'Introduce yourself'
    print("Audio Processed \n\n")
    api_request_json["messages"].append({"role": "user", "content": prompt})
    response = llama.run(api_request_json)
    responseArray = json.dumps(response.json()["choices"][0]["message"]["content"]).replace('"', '').split("$")
    print(responseArray[0])
    api_request_json["messages"].append({"role": "system", "content": responseArray[0]})
    array = responseArray[1].replace(" ", "").split(',')
    for i in array:
        try:
            eval(i)
        except:
            print("Error in function")