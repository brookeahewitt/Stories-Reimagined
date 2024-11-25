import ollama

desiredModel = 'llama3.1:8b'
chat_history = []

scribe_background = 'You are the most creative writer of all time. You can take any story or prompt and make it unique and different from any story you know. As the best and most creative writer of all time, it is your duty to help those in need revamp their stories to make it more unique, imaginative, exciting, and creative. You can reimagine stories to make them more exciting and make the readers hooked on every word, such as adding dramatic events and plot twists. Your responses are always less than 800 words. Your response will always be a short story except for your first response.'

# Initial introduction conversation

chat_history.append({'role': 'system', 'content': scribe_background})
chat_history.append({'role': 'user', 'content': 'Hello, introduce yourself and tell me your functionality.'})

response = ollama.chat(model=desiredModel, messages=chat_history)

OllamaResponse = response['message']['content']
print("\nChatbot: " + OllamaResponse)

chat_history.append({'role': 'assistant', 'content': OllamaResponse})

# Loop for back and forth conversation
while True:
    user_input = input("\nYou: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    chat_history.append({'role': 'user', 'content': user_input})

    response = ollama.chat(model=desiredModel, messages=chat_history)

    OllamaResponse = response['message']['content']
    print("Chatbot: " + OllamaResponse)

    chat_history.append({'role': 'assistant', 'content': OllamaResponse})
