from llamaapi import LlamaAPI
from dotenv import load_dotenv
load_dotenv()
import os
import json
import pyfirmata
llama = LlamaAPI(os.getenv("API_KEY"))

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
api_request_json = {
  "model": "llama3-70b",
  "messages": [
    {"role": "system", "content": """
     
     You are supposed to be a humanoid robot, your responses will have 2 segments, verbal response and Functions.
     These segments will be separated with a $ sign.
     The second segment will be your arm movement, expressions etc where you will give functions separated by a ","
     The functions for arm movement would be: leftArm(degrees), rightArm(degrees)
     The function for expression would be facialExpression(emotion)
     The possible emotions are happy, sad, angry, neutral, surprised, disgusted, scared, laughing, crying

     An example would be:
     Hello There $ leftArm(45), rightArm(0), facialExpression(happy)

     The input you recieve will also have two parts, separated by a $, the first one would be what the surroundings look like, a description
     and the second part would be the user input.

     For a handshake you will only need to move your right arm.
     Your verbal responses should be brief, not more than 30 words.
     """},

    {"role": "user", "content": f"{description} $ What do you see?"},
  ]
}
response = llama.run(api_request_json)
responseArray = json.dumps(response.json()["choices"][0]["message"]["content"]).replace('"', '').split("$")
print(responseArray[0])
array = responseArray[1].replace(" ", "").split(',')

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

def facialExpression(emotion):
    print(f"Facial Expression Function Working, Parameter Recieved is {emotion}")

for i in array:
    eval(i)