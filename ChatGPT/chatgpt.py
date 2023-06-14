import openai
import config

openai.api_key = config.SECRET_KEY
def query(prompt):
    message = [{"role": "user", "content": prompt}]

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    reply = chat.choices[0].message.content
    return reply