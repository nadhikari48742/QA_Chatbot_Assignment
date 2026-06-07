from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create chatbot
chatbot = ChatBot("StudentBot")

# Train chatbot with custom responses
trainer = ListTrainer(chatbot)

trainer.train([
    "Hello",
    "Hi there!",
    "How are you?",
    "I am doing well, thank you for asking.",
    "What is your name?",
    "My name is StudentBot.",
    "Goodbye",
    "See you later!"
])

print("Type 'bye' to exit")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print("Bot:", response)