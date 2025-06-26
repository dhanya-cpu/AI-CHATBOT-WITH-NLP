import spacy
nlp = spacy.load("en_core_web_sm")
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thanks", "thank you"],
    "name": ["what is your name", "who are you"],
    "function": ["what can you do", "your purpose", "what is your function"],
}
responses = {
    "greeting": "Hey! How can I help you today? ",
    "goodbye": "Goodbye! Have a great day! ",
    "thanks": "You're welcome!",
    "name": "I'm your NLP chatbot powered by spaCy!",
    "function": "I can chat with you, answer simple questions, and be awesome ",
    "unknown": "Sorry, I didn’t understand that. Can you rephrase?"
}
def get_intent(user_input):
    user_input = user_input.lower()
    doc = nlp(user_input)
    for intent, patterns in intents.items():
        for pattern in patterns:
            if pattern in user_input:
                return intent
    return "unknown"
print(" Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("👤 You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print(" Chatbot:", responses["goodbye"])
        break
    intent = get_intent(user_input)
    print("Chatbot:", responses[intent])
