import base64
import requests
import os

# OpenAI API Key
api_key = my_secret = os.environ['OPENAI_API_KEY']

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# User inputs
image_path = "./uploads/" + input('Enter the path of the image in the uploads folder: ')
text_prompt = input("Enter the text prompt: ")
if text_prompt == '': 
  text_prompt = "What's in this image?"


text_prompt = f"{text_prompt}. The file name of the provided image is {image_path.split('/')[-1]}"
text_prompt = text_prompt.replace('?.', '?').replace('!.', '!')

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": text_prompt
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

responseJson = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

response = responseJson.json()
choices = response['choices']
for choice in choices:
  finish_reason = choice['finish_reason']
  if (finish_reason == 'stop'):
    message = choice['message']
    role = message['role']
    content = message['content']
    output = f"\nRole: {role}\n\nContent: \n{content}\n"
    print(output)