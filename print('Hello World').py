chatbot_name="Bot 1"
responses={
    "hi":"Hi there ! How can I help you ?",
    "hello":"Hello ! How can I help you ?",
    "howareyou":"I am good.",
    "whatisyourname": f"My name is {chatbot_name}",
    "bye": "Goodbye ! Have a great day !",
    "goodbye": "Goodbye ! Have a great day !",
    "thankyou": "You're very welcome !",
    "thanks": "Anytime ! Happy to help !",
    "whatcanyoudo": "I can chat with you and answer simple questions !",
    "help": "Tell me what you need, and I will do my best to help !",
    "goodmorning": "Good morning ! How is your day starting out ?",
    "goodafternoon": "Good afternoon ! How can I help you today ?",

}

print("Bot 1: How Can I Help You Today ? ")

while True:
    
    message=input("You: ").replace(" ","").lower()

    if message in ["bye","quit","exit"]:
        print("Bot: bye ")
        break

    reply=responses.get(message, "Sorry, I don't understand that.")
    print(f"Bot 1: {reply}")
