from ChatGPT import chatgpt#ChatGPT folder
import Twilio #Twilio folder

while(1):
    question = input("Type your question here: ")
    response = chatgpt.query(question)
    print("ChatGPT response: ", response)