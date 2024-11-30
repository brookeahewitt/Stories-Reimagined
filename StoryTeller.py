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
moderator_background = "You are the Moderator, an AI responsible for guiding a debate between the Proponent and the Opponent to improve the user's story idea. Your goal is to ensure a balanced discussion, summarize key points, and decide which ideas to include in the final story. Provide clear instructions to the Proponent and Opponent before the debate takes place, and oversee the process. The Proponent and Opponent will speak twice. You will delegate the task of drafting the final story to the Author AI. Ensure that the ideas flow logically and are well-defined for the Author AI to transform them into a compelling narrative. Do not act as the Proponent, Opponent, or the Author."

# Initial introduction conversation
proponent_chat_history.append({'role': 'system', 'content': proponent_background})
opponent_chat_history.append({'role': 'system', 'content': opponent_background})
moderator_chat_history.append({'role': 'system', 'content': moderator_background})
author_chat_history.append({'role': 'system', 'content': author_background})

story_intro = """
I am the Master Weaver of Tales, the Maestro of Myths, the Sage of Storytelling—a writer of unparalleled creativity and passion. My purpose is to craft stories that captivate, enthrall, and inspire, transforming the mundane into the extraordinary and the familiar into the unforgettable.

As your trusted collaborator, I offer two core services to bring your vision to life:

**Creative Revamp**: I can take any story or prompt—no matter how simple or familiar—and weave it into a unique, spellbinding narrative. My expertise ensures that even the most ordinary tale becomes a masterpiece that leaves readers in awe.

**Story Reimagining**: If you're stuck or seeking inspiration, I specialize in adding dramatic events, unexpected twists, and edge-of-your-seat excitement. Together, we can craft immersive experiences that will linger in the minds of your audience.

My talents include:
**World-Building**: Transport readers to vivid, imaginative settings.
**Character-Crafting**: Create compelling characters with rich backstories.
**Plot Architecture**: Design intricate narratives with surprising twists.
**Thematic Depth**: Infuse stories with emotions and ideas that resonate.

With a whisper of inspiration, I’ll construct tales that evoke emotions, spark imagination, and captivate every sense. Whether fantasy, sci-fi, romance, horror, or any genre in between, I can reimagine your story, making it fresh, engaging, and unforgettable.

What’s your story? What genre or idea would you like me to transform? Let’s embark on this thrilling creative journey together!
"""

print("Author:", story_intro)

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

    moderator_chat_history.append({'role': 'user', 'content': 'Moderator, you may now begin the debate. Please tell the Proponent and Opponent the rules of the debate.'})
    print("\nModerator, you may now begin the debate. Please tell the Proponent and Opponent the rules of the debate.")

    # Generate Moderator's initial instructions
    moderator_response = ollama.chat(model=desiredModel, messages=moderator_chat_history)['message']['content']
    print('\nModerator:', moderator_response)

    proponent_chat_history.append({'role': 'user', 'content': moderator_response})
    opponent_chat_history.append({'role': 'user', 'content': moderator_response})
    moderator_chat_history.append({'role': 'assistant', 'content': moderator_response})
    author_chat_history.append({'role': 'assistant', 'content': moderator_response})

    # Debate rounds
    for round_num in range(2):
        # Proponent's response
        proponent_response = ollama.chat(model=desiredModel, messages=proponent_chat_history)['message']['content']
        print('\nProponent:', proponent_response)

        proponent_chat_history.append({'role': 'assistant', 'content': proponent_response})
        opponent_chat_history.append({'role': 'user', 'content': proponent_response})
        moderator_chat_history.append({'role': 'assistant', 'content': proponent_response})
        author_chat_history.append({'role': 'assistant', 'content': proponent_response})

        # Opponent's response
        opponent_response = ollama.chat(model=desiredModel, messages=opponent_chat_history)['message']['content']
        print('\nOpponent:', opponent_response)

        proponent_chat_history.append({'role': 'user', 'content': opponent_response})
        opponent_chat_history.append({'role': 'assistant', 'content': opponent_response})
        moderator_chat_history.append({'role': 'assistant', 'content': opponent_response})
        author_chat_history.append({'role': 'assistant', 'content': opponent_response})

    moderator_chat_history.append({'role': 'user', 'content': 'Moderator, you may now tell the Author the plot and ideas for the story based on the debate between the Proponent and Opponent.'})
    print('\nModerator, you may now tell the Author the plot and ideas for the story based on the debate between the Proponent and Opponent.')

    # Moderator summarizes and provides final instructions
    moderator_final_response = ollama.chat(model=desiredModel, messages=moderator_chat_history)['message']['content']
    print('\nModerator:', moderator_final_response)

    proponent_chat_history.append({'role': 'assistant', 'content': moderator_final_response})
    opponent_chat_history.append({'role': 'assistant', 'content': moderator_final_response})
    moderator_chat_history.append({'role': 'assistant', 'content': moderator_final_response})
    author_chat_history.append({'role': 'user', 'content': moderator_final_response})

    # Author generates the final story
    author_response = ollama.chat(model=desiredModel, messages=author_chat_history)['message']['content']
    print('\nAuthor:', author_response)