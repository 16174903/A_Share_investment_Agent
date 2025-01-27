
import google.generativeai as genai

genai.configure(api_key='AIzaSyCj8Beo4pu-DUFHKPFoSJKE3bjY2AP_9yE')

response = genai.chat(messages=["Hello."])
print(response.last)  # 'Hello! What can I help you with?'
response.reply("Can you tell me a joke?")