import ollama
from ToT.ToTstruct import *
import random

def ToTloop(given_story = None, human_response = True, max_depth = 2):

    desiredModel = 'llama3.1:8b'

    # Set the system message to define the chatbot's creative background
    scribe_background = 'You are the most creative writer of all time. You can take any story or prompt and make it unique and different from any story you know. As the best and most creative writer of all time, it is your duty to help those in need revamp their stories to make it more unique, imaginative, exciting, and creative. You can reimagine stories to make them more exciting and make the readers hooked on every word. Your responses are always around or within 800 words.'

    # Uneeeded as StoryTeller.py introduces themselves. Keeping just in case
    # # Initialize conversation with a chatbot prompt
    # response = ollama.chat(model=desiredModel, messages=[
    #     {
    #         'role': 'system',
    #         'content': scribe_background,
    #     },
    #     {
    #         'role': 'user',
    #         'content': 'Introduce yourself based on your background.',
    #     }
    # ])

    # Taken care of by func. Keeping just in case
    # max_depth = int(input("Please input the max depth of ToT:"))
    # max_depth = 2

    # OllamaResponse = response['message']['content']
    # print("Author: " + OllamaResponse)

    # Now, loop to allow back and forth conversation
    for i in range(max_depth+1):

        # Get user input for the next prompt
        if human_response:
            if ((i == 0) & (given_story is not None)): 
                user_input = given_story
                print("Story Received, Sending")
            else:
                user_input = input("\nYou: ")
        else: #random response
            if ((i == 0) & (given_story is not None)): 
                user_input = given_story
                print("Story Received, Sending")
            else:
                max_num_stories = i * 3
                story_reaction = random.randint(1,4)
                ## Liked one,
                if story_reaction == 1:
                    story_1_num = random.randint(1,max_num_stories)
                    user_input = f"I liked Story {story_1_num} the best!"
                ## Liked two, combine
                elif story_reaction == 2:
                    story_1_num = random.randint(1,max_num_stories)
                    story_2_num = random.randint(1,max_num_stories)
                    while story_1_num == story_2_num: #if they match, reroll
                        story_2_num = random.ranint(1,max_num_stories)
                    user_input = f"I liked Story {story_1_num} and Story {story_2_num}. Combine them!"
                ## Disliked one, liked one
                elif story_reaction == 3:
                    story_1_num = random.randint(1,max_num_stories)
                    story_2_num = random.randint(1,max_num_stories)
                    while story_1_num == story_2_num: #if they match, reroll
                        story_2_num = random.ranint(1,max_num_stories)
                    user_input = f"I liked Story {story_1_num} , but I also disliked Story {story_2_num}."
                ## Disliked one
                else:
                    story_1_num = random.randint(1,max_num_stories)
                    user_input = f"I disliked Story {story_1_num} "
                
                print(f"Response: {user_input}")
                
            

        # # Exit condition for the loop (user types 'exit' to end the conversation)
        # if user_input.lower() == 'exit':
        #     print("Goodbye!")
        #     break
        
        # initialize Tree if first time
        if i == 0:
            ThoughtTree = ToTStories(user_input, max_depth)

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

        print("LLM Response: " + OllamaResponse)

        depth = ThoughtTree.parse_LLM(OllamaResponse)

    final_story_pattern = r"\*\*.*?\*\*\n(.*?)\n\*\*The End\*\*"

    match = re.search(final_story_pattern, OllamaResponse, re.DOTALL)

    if match:
        print("Final Story Found!")
        final_story = match.group(1).strip()
        print(final_story) #for debugging
    else:
        print("No final story found.")

    print("Tree of Thoughts Finished!")

    return final_story