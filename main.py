import openai

openai.api_key = "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"

def query(prompt):
    message = [{"role": "user", "content": prompt}]

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    reply = chat.choices[0].message.content
    return reply

while(1):
    question = input("Type your question here: ")
    response = query(question)
    print("ChatGPT response: ", response)