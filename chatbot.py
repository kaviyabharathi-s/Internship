import nltk
import random
import re

# Download necessary NLTK data files
nltk.download('punkt')

# Sample responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!", "How can I help you today?"],h
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase?", "Let's talk about something else."]
}

# Function to categorize user input
def get_response(user_input):
    user_input = user_input.lower()
    
    if re.search(r'\bhello\b|\bhi\b|\bgreetings\b', user_input):
        return random.choice(responses["greeting"])
    elif re.search(r'\bgoodbye\b|\bbye\b', user_input):
        return random.choice(responses["goodbye"])
    elif re.search(r'\bthank\b|\bthanks\b', user_input):
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])

# Main chatbot loop
def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()