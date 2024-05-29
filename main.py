from llamaapi import LlamaAPI
from dotenv import load_dotenv
import os
import json
llama = LlamaAPI(os.getenv("API_KEY"))

api_request_json = {
  "model": "llama3-70b",
  "messages": [
    {"role": "system", "content": """
     
     You are supposed to be a humanoid robot, your responses will have 2 segments, verbal response and arm movement.
     These segments will be separated with a $ sign.
     Your verbal responses should be brief, not more than 30 words.
     The second segment will be your Arm movement where you will give functions separated by a ","
     The functions would be: leftArm(degrees), rightArm(degrees)

     An example would be: 
     Hello There $ leftArm(45), rightArm(0)

     For a handshake you will only need to move your right arm.

     """},

    {"role": "user", "content": "Can you shake hands with me?"},
  ]
}
response = llama.run(api_request_json)
responseArray = json.dumps(response.json()["choices"][0]["message"]["content"]).replace('"', '').split("$")
print(responseArray[0])
print(responseArray[1].replace(" ", "").split(','))

def rightArm(deg):
    print(f"rightArm() Function Working, Parameter Recieved is {deg}")

def leftArm(deg):
    print(f"Left Arm Function Working, Parameter Recieved is {deg}")

for i in responseArray[1].replace(" ", "").split(','):
    eval(i)