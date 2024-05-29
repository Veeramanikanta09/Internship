import nltk
from nltk.chat.util import reflections

# Download required resources
nltk.download('punkt')
nltk.download('wordnet')

# Define greetings and reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!"]
    ],
    [
        r"what is your name?",
        ["My name is Chatty the Chatbot."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thanks for asking! How are you?"]
    ],
    [
        r"(.*) weather (.*)",
        ["Sorry, I can't provide weather information yet, but I'm still learning!"]
    ],
    [
        r"what is your purpose?",
        ["I am a simple chatbot designed to have basic conversations."]
    ],
]

# Define chatbot reflection function
def chatbot(reflections_list, user_input):
  chatbot_response = ""
  for (pattern, response) in reflections_list:
    if nltk.chat.util.match(pattern, user_input):
      chatbot_response = random.choice(response)
      return chatbot_response

  # Default response for unmatched patterns
  return "Sorry, I don't understand. Can you rephrase that?"

# Start the chat loop
print("Hi! I'm Chatty, the chatbot. How can I help you today?")
while True:
  user_input = input("> ")
  chatbot_response = chatbot(pairs, user_input)
  print(chatbot_response)

