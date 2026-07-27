print("Welcome to Mini Chatbot!")

message = input("You: ").strip().lower()

if message == "hello":
    print("Bot: Hi!")
elif message == "how are you":
    print("Bot: I'm fine, thanks!")
elif message == "bye":
    print("Bot: Goodbye!")
else:
    print("Bot: Sorry, I don't understand.")
