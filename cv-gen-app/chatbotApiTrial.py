from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
  "email": "email",
  "password": "password"
})


response = ""
while(True):
    prompt = input("ask: ")
    for data in chatbot.ask(
      prompt
    ):
        response = data["message"]

    print(response)
