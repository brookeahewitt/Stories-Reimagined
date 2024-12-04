import ollama
from MAD.MADprompts import story_intro_prompt
from MAD.MADstruct import initialize_chat_history, MAD_loop

# This file includes the ToT-to-MAD pipeline

# Initialize chat history
proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history = initialize_chat_history()
print("Author:", story_intro)


# Can implement ToT here and get a result to feed into MAD 
ToT_result = None


# Can leave ToT_result as None if want to run MAD loop by itself
MAD_loop(ToT_result, proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history)