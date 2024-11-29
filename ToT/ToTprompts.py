def starting_prompt(user_input):

    g_prompt = '''Write 3 stories based on the following given idea or story: {input}

    Each story should be labeled numerically in the following format:

    Story 1) Your first story idea here

    Story 2) Your second story idea here 

    Story 3) Your third story idea here

    Finally, ask me at the end "Would like to expand on these ideas? Please mention which story you liked or disliked with the appropriate number."
    '''

    return g_prompt.format(input=user_input)

def critique_prompt(user_input, story_nodes_list):

    #TODO: parse given story node list, add to the prompt, make sure to have the new story format start with the new highest id

    #TODO Finish creating critique prompt
    c_prompt = '''Create or adjust 3 new stories based on the following critique: {u_input}

    The critique is referencing these stories: {stories} 

    Each story should be labeled numerically starting with the number "{new_max_id}" in the following format:


    
    
    
    '''

    #TODO: format c_prompt

    return c_prompt

def finish_prompt(user_input, story_nodes_list):

    #TODO: Write a prompt that writes the ultimate story based on all the past critique

    f_prompt='''

    '''
    #TODO: format f_prompt

    return f_prompt