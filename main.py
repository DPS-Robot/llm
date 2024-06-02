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


chatlog = ""
def facialExpression(emotion):
    print(f"Facial Expression Function Working, Parameter Recieved is {emotion}")

while True:
    prompt = transcribe(record_audio())
    print("Audio Processed \n\n")
    chatlog += f"User: {prompt}\n"
    api_request_json = {
        "model": "llama3-70b",
        "messages": [
            {"role": "system", "content": f"""
     
             Previous Chats for Context:
             {chatlog}

             

            You are supposed to be a humanoid robot, your responses will have 2 segments, verbal response and Functions.
            These segments will be separated with a $ sign.
            The second segment will be your arm movement, expressions etc where you will give functions separated by a ","
            The functions for arm movement would be: leftArm(degrees), rightArm(degrees)
            The function for expression would be facialExpression(emotion)
            The possible emotions are happy, sad, angry, neutral, surprised, disgusted, scared, laughing, crying
            YOU ARE NOT ALLOWED TO GIVE ANY EXPRESSION THAT IS NOT IN THIS LIST

            An example would be:
            Hello There $ leftArm(45), rightArm(0), facialExpression(happy)

            The input you recieve will also have two parts, separated by a $, the first one would be what the surroundings look like, a description
            and the second part would be the user input.

            For a handshake you will only need to move your right arm.
            Your verbal responses should be brief, not more than 30 words.
            """},

            {"role": "user", "content": f"{description} $ {prompt}"},
        ]
    }
    response = llama.run(api_request_json)
    responseArray = json.dumps(response.json()["choices"][0]["message"]["content"]).replace('"', '').split("$")
    print(responseArray[0])
    chatlog += f"Robot: {responseArray[0]}\n"
    array = responseArray[1].replace(" ", "").split(',')
    for i in array:
        try:
            eval(i)
        except:
            print("Error in function")