import ollama
from MADprompts import author_background_prompt, proponent_background_prompt, opponent_background_prompt, moderator_background_prompt

# ollama server
desiredModel = 'llama3.1:8b'

# Initialize chat histories for each role
def initialize_chat_history():
    proponent_chat_history = []
    moderator_chat_history = []
    opponent_chat_history = []
    author_chat_history = []

    # Initial introduction conversation
    roles = ['system', 'system', 'system', 'system']
    strings = [proponent_background_prompt(), opponent_background_prompt(), moderator_background_prompt(), author_background_prompt()]
    proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history = update_chat_history(proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history, roles, strings)

    return proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history


def update_chat_history(proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history, roles, strings):
    proponent_chat_history.append({'role': roles[0], 'content': strings[0]})
    opponent_chat_history.append({'role': roles[1], 'content': strings[1]})
    moderator_chat_history.append({'role': roles[2], 'content': strings[2]})
    author_chat_history.append({'role': roles[3], 'content': strings[3]})

    return proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history


def update_moderator(moderator_chat_history, role, string):
    moderator_chat_history.append({'role': role, 'content': string})
    return moderator_chat_history


# Loop for back and forth conversation
def MAD_loop(ToT_result=None, proponent_chat_history=[], moderator_chat_history=[], opponent_chat_history=[], author_chat_history=[]):
    i = 0

    while True:
        if i == 0 and ToT_result is None:
            user_input = "\nYou: " + ToT_result
        else:
            user_input = input("\nYou: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Add user input to all chat histories
        roles = ['user', 'user', 'user', 'user']
        strings = [user_input, user_input, user_input, user_input]
        proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history = update_chat_history(proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history, roles, strings)

        role = 'user'
        string = 'Moderator, you may now begin the debate. Please tell the Proponent and Opponent the rules of the debate.'
        update_moderator(moderator_chat_history, role, string)
        print("\nModerator, you may now begin the debate. Please tell the Proponent and Opponent the rules of the debate.")

        # Generate Moderator's initial instructions
        moderator_response = ollama.chat(model=desiredModel, messages=moderator_chat_history)['message']['content']
        print('\nModerator:', moderator_response)

        roles = ['user', 'user', 'assistant', 'assistant']
        strings = [moderator_response, moderator_response, moderator_response, moderator_response]
        update_chat_history(proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history, roles, strings)

        # Debate rounds
        for round_num in range(2):
            # Proponent's response
            proponent_response = ollama.chat(model=desiredModel, messages=proponent_chat_history)['message']['content']
            print('\nProponent:', proponent_response)

            roles = ['assistant', 'user', 'assistant', 'assistant']
            strings = [proponent_response, proponent_response, proponent_response, proponent_response]
            update_chat_history(proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history, roles, strings)

            # Opponent's response
            opponent_response = ollama.chat(model=desiredModel, messages=opponent_chat_history)['message']['content']
            print('\nOpponent:', opponent_response)

            roles = ['user', 'assistant', 'assistant', 'assistant']
            strings = [opponent_response, opponent_response, opponent_response, opponent_response]
            update_chat_history(proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history, roles, strings)

        moderator_chat_history.append({'role': 'user', 'content': 'Moderator, you may now tell the Author the plot and ideas for the story based on the debate between the Proponent and Opponent.'})
        print('\nModerator, you may now tell the Author the plot and ideas for the story based on the debate between the Proponent and Opponent.')

        # Moderator summarizes and provides final instructions
        moderator_final_response = ollama.chat(model=desiredModel, messages=moderator_chat_history)['message']['content']
        print('\nModerator:', moderator_final_response)

        roles = ['assistant', 'assistant', 'assistant', 'user']
        strings = [moderator_final_response, moderator_final_response, moderator_final_response, moderator_final_response]
        update_chat_history(proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history, roles, strings)

        # Author generates the final story
        author_response = ollama.chat(model=desiredModel, messages=author_chat_history)['message']['content']
        print('\nAuthor:', author_response)