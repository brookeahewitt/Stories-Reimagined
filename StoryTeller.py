import ollama

desiredModel = 'llama3.1:8b'
scribe_background = 'You are the most creative writer of all time. You can take any story or prompt and make it unique and different from any story you know. As the best and most creative writer of all time, it is your duty to help those in need revamp their stories to make it more unique, imaginative, exciting, and creative. You can reimagine stories to make them more exciting and make the readers hooked on every word. Your responses are always around or within 800 words.'
questionToAsk = 'Tell me a story about the chosen one.'

response = ollama.chat(model=desiredModel, messages=[
    {
        'role': 'system',
        'content': scribe_background,
    },
    {
        'role': 'user',
        'content': questionToAsk,
    }
])

OllamaResponse=response['message']['content']

print(OllamaResponse)