def starting_prompt(user_input):

    g_prompt = '''Write 3 stories based on the following given idea or story: {input}

    Each story should be labeled numerically in the following format:

    Story 1: Your first story idea here

    Story 2: Your second story idea here 

    Story 3: Your third story idea here

    Finally, ask me at the end "Would like to expand on these ideas? Please mention which story you liked or disliked with the appropriate number (for example, 'story 1 is good but story 2 is bad')."
    '''

    return g_prompt.format(input=user_input)

def critique_prompt(user_input, story_nodes_list, highest_id):

    #TODO: parse given story node list, add to the prompt, make sure to have the new story format start with the new highest id
    stories = "\n".join([f"Story {node.id}: {node.story}" for node in story_nodes_list])

    c_prompt = f'''Create or adjust 3 new stories based on the following critique: {user_input}

    The critique is referencing these stories: {stories}  

    Each story should be labeled numerically increasing by 1 starting with the number "{highest_id+1}" in the following starting format:

    Story {highest_id+1}: Your first story here

    Story {highest_id+2}: Your second story here

    Story {highest_id+3}: Your third story here
    
    Finally, ask me at the end "Would like to expand on these ideas? Please mention which story you liked or disliked with the appropriate number (for example, 'story 1 is good but story 2 is bad')."
    '''

    return c_prompt

def finish_prompt(user_input, story_nodes_list):

    #TODO: Write a prompt that writes the ultimate story based on all the past critique

    stories = "\n".join([f"Story {node.id}: {node.story}" for node in story_nodes_list])

    f_prompt=f'''Create a final long story under 800 words based on this critique: {user_input}

    The critique is referencing these stories: {stories}  

    Your output should only be a story and should be labeled in the following format:

    **Story:Your story title here** Your story here

    Finally, end the story with **The End**
    '''

    return f_prompt