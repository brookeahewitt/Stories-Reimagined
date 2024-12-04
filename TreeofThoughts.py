import ollama
from ToT.ToTstruct import *

desiredModel = 'llama3.1:8b'

# Set the system message to define the chatbot's creative background
scribe_background = 'You are the most creative writer of all time. You can take any story or prompt and make it unique and different from any story you know. As the best and most creative writer of all time, it is your duty to help those in need revamp their stories to make it more unique, imaginative, exciting, and creative. You can reimagine stories to make them more exciting and make the readers hooked on every word. Your responses are always around or within 800 words.'


# Initialize conversation with a chatbot prompt
response = ollama.chat(model=desiredModel, messages=[
    {
        'role': 'system',
        'content': scribe_background,
    },
    {
        'role': 'user',
        'content': 'Introduce yourself based on your background.',
    }
])

OllamaResponse = response['message']['content']
print("Chatbot: " + OllamaResponse)



# Now, loop to allow back and forth conversation
for i in range(10):
    # Get user input for the next prompt
    user_input = input("\nYou: ")

    # Exit condition for the loop (user types 'exit' to end the conversation)
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # initialize Tree if first time
    if i == 0:
        ThoughtTree = ToTStories(user_input)

    #Get prompt
    user_prompt = ThoughtTree.return_stories(user_input)

    
    # Send user input to Ollama for response
    response = ollama.chat(model=desiredModel, messages=[
        {
            'role': 'system',
            'content': scribe_background,
        },
        {
            'role': 'user',
            'content': user_prompt,
        }
    ])

    # Get the chatbot's response
    OllamaResponse = response['message']['content']

    print("Chatbot: " + OllamaResponse)

    depth = ThoughtTree.parse_LLM(OllamaResponse)

    print("Chatbot: " + OllamaResponse)
    
    if depth == ThoughtTree.max_depth:
        break