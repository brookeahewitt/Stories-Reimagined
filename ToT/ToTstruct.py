from ToTprompts import * 

'''
BREAKDOWN:

Create ToTStories, which holds the id nodes and each "story" generated by the LLM.

Parse through responses of LLM to find each "story" it generates, and add it to the tree. (parse_LLM)

Each time it gets a user input, it parses through the user input to find the story labels 
associated with the story, and return appropriate prompt (return_stories)


'''

class ThoughtNode():
    def __init__(self, id, story, parent=None):
        self.id = id
        self.story = story
        self.parent = parent
        self.children = []

    def add_child(self, id, story):
        child_node = ThoughtNode(id, story, parent=self)
        self.children.append(child_node)
        return child_node

class ToTStories():

    def __init__(self, starting_user_input, max_depth = 5):
        self.root = ThoughtNode(0, starting_prompt(starting_user_input))
        self.depth = 0 #tracks response amount of conversation, default of 5
        self.max_depth = max_depth 

    def parse_LLM(llm_response):
         # TODO: Parse response to find the delimiters "story #)" and attach to appropriate Node
        if self.depth > self.max_depth: #Max depth reached!
             return None

        self.depth +=1
        return self.depth
    
    def return_stories(user_response):
         # TODO: Return appropriate prompt (based on user_response) and attached stories to said prompt 
        
        if self.depth > self.max_depth:
            
            return #final prompt here!
        
        return #critique prompt here!

    

    

    

