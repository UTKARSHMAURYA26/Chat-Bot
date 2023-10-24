import random

# Define a dictionary of responses
responses = {
    "hello": ["Hey! I am ChatBot for SkillSync Interns.", "Hello there!", "Hi! How can I assist you today?"],
    "how are you": ["I'm good, thanks!", "I'm just a computer program, so I don't have feelings, but I'm here to help!", "I'm functioning perfectly, thanks for asking."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!", "Farewell!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "what's your name": ["I'm ChatBot.", "I don't have a name, but you can call me ChatBot.", "I go by ChatBot."],
    "who created you": ["I was created by SkillSync Interns.", "The creators of SkillSync Interns designed me.", "I'm a product of SkillSync Interns."],
    "what's the weather like": ["I'm sorry, I don't have access to real-time data.", "You can check a weather website or app for the latest information."],
    "tell me a joke": ["Why was the math book sad? Because it had too many problems!", "How does a computer get drunk? It takes screenshots!"],
    "tell me a fact": ["Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!", "Here's a fact: The Earth is not a perfect sphere; it's slightly flattened at the poles and bulging at the equator."],
    "what's your favorite color": ["I'm just a computer program, so I don't have a favorite color, but I can assist you with various tasks!"],
    "how old are you": ["I don't have an age in the traditional sense, but I was created recently to help you!"],
    "tell me a riddle": ["Sure, here's a riddle: I'm taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I? Answer: A pencil lead!", "Here's a riddle: The more you take, the more you leave behind. What am I? Answer: Footsteps in the sand!"],
    "what's your purpose": ["My purpose is to assist you with information and engage in friendly conversations. How can I help you today?"],
    "where are you from": ["I don't have a specific location. I exist in the digital world to assist you."],
    "how can I contact you": ["You can't contact me directly, but I'm here to respond to your questions and engage in conversations. Just type your query!"],
    "do you dream": ["I'm just a computer program, so I don't dream, but I'm here to help with your queries."],
    "what's your favorite food": ["I don't eat, so I don't have a favorite food, but I can help you find recipes or food-related information!"],
    "tell me a fun fact": ["Here's a fun fact: Octopuses have three hearts!", "Did you know that honey never spoils and can be preserved for thousands of years? It's pretty amazing!"],
    "can you sing a song": ["I'm not programmed to sing, but I can provide you with song lyrics or information about your favorite songs!"],
    "default": ["I'm not sure what you mean.", "Could you please rephrase that?", "I don't understand."],
}

# Function to get a response for user input
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user input matches any predefined keys in the dictionary
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # If no match is found, provide a default response
    return random.choice(responses["default"])

# Starting response
print("ChatBot: Hello! I'm ChatBot for SkillSync Interns. How can I assist you today?")

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatBot: Goodbye!")
        break
    response = get_response(user_input)
    print("ChatBot:", response)
