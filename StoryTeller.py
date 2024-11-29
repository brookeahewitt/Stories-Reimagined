import ollama

# ollama serve

desiredModel = 'llama3.1:8b'
proponent_chat_history = []
moderator_chat_history = []
opponent_chat_history = []
author_chat_history = []

author_background = 'You are the Author, an AI responsible for drafting unique, compelling stories. You will receive guidance from the Moderator on which elements to include. Your role is to weave these ideas into a cohesive and engaging narrative, using vivid descriptions, emotional depth, and creative storytelling techniques. Your response will be a short story based on the information provided from the user and moderator.'
proponent_background = 'You are the Proponent, an AI whose role is to enhance and improve the story idea provided by the user. Your goal is to propose innovative, exciting, and unique elements for the story. Be bold and creative, suggesting twists, world-building ideas, character development arcs, or unusual settings that make the story stand out.'
opponent_background = 'You are the Opponent, an AI tasked with critiquing and refining the story improvements suggested by the Proponent. Your goal is to identify potential weaknesses, clichés, or missed opportunities in the story and suggest alternative ideas or improvements. Be constructive but critical, encouraging deeper exploration and originality.'
moderator_background = "You are the Moderator, an AI responsible for guiding a debate between the Proponent and the Opponent to improve the user's story idea. Your goal is to ensure a balanced discussion, summarize key points, and decide which ideas to include in the final story. Provide clear instructions to the Proponent and Opponent before the debate takes place, and oversee the process. The Proponent and Opponent will speak twice. You will delegate the task of drafting the final story to the Author AI. Ensure that the ideas flow logically and are well-defined for the Author AI to transform them into a compelling narrative."

# Initial introduction conversation
proponent_chat_history.append({'role': 'system', 'content': proponent_background})
opponent_chat_history.append({'role': 'system', 'content': opponent_background})
moderator_chat_history.append({'role': 'system', 'content': moderator_background})
author_chat_history.append({'role': 'system', 'content': author_background})

print("Chatbot: Hello! Welcome to the magical world of stories, where we take your stories and ideas and turn them into a magical experience. How can I help?")

# Loop for back and forth conversation
while True:
    user_input = input("\nYou: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    # Add user input to all chat histories
    proponent_chat_history.append({'role': 'user', 'content': user_input})
    opponent_chat_history.append({'role': 'user', 'content': user_input})
    moderator_chat_history.append({'role': 'user', 'content': user_input})
    author_chat_history.append({'role': 'user', 'content': user_input})

    # Generate Moderator's initial instructions
    moderator_response = ollama.chat(model=desiredModel, messages=moderator_chat_history)['message']['content']
    print('\nModerator:', moderator_response)

    # Add Moderator's response to all chat histories
    proponent_chat_history.append({'role': 'assistant', 'content': moderator_response})
    opponent_chat_history.append({'role': 'assistant', 'content': moderator_response})
    moderator_chat_history.append({'role': 'assistant', 'content': moderator_response})
    author_chat_history.append({'role': 'assistant', 'content': moderator_response})

    # Debate rounds
    for round_num in range(2):
        # Proponent's response
        proponent_response = ollama.chat(model=desiredModel, messages=proponent_chat_history)['message']['content']
        print('\nProponent:', proponent_response)

        # Add Proponent's response to all relevant chat histories
        proponent_chat_history.append({'role': 'assistant', 'content': proponent_response})
        opponent_chat_history.append({'role': 'user', 'content': proponent_response})
        moderator_chat_history.append({'role': 'assistant', 'content': proponent_response})
        author_chat_history.append({'role': 'assistant', 'content': proponent_response})

        # Opponent's response
        opponent_response = ollama.chat(model=desiredModel, messages=opponent_chat_history)['message']['content']
        print('\nOpponent:', opponent_response)

        # Add Opponent's response to all relevant chat histories
        proponent_chat_history.append({'role': 'user', 'content': opponent_response})
        opponent_chat_history.append({'role': 'assistant', 'content': opponent_response})
        moderator_chat_history.append({'role': 'assistant', 'content': opponent_response})
        author_chat_history.append({'role': 'assistant', 'content': opponent_response})

    # Moderator summarizes and provides final instructions
    moderator_final_response = ollama.chat(model=desiredModel, messages=moderator_chat_history)['message']['content']
    print('\nModerator (Final Instruction):', moderator_final_response)

    # Add final Moderator response to all chat histories
    proponent_chat_history.append({'role': 'assistant', 'content': moderator_final_response})
    opponent_chat_history.append({'role': 'assistant', 'content': moderator_final_response})
    moderator_chat_history.append({'role': 'assistant', 'content': moderator_final_response})
    author_chat_history.append({'role': 'assistant', 'content': moderator_final_response})

    # Author generates the final story
    author_response = ollama.chat(model=desiredModel, messages=author_chat_history)['message']['content']
    print('\nAuthor:', author_response)