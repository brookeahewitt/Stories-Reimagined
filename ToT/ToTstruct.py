from .ToTprompts import * 
import re

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
        self.root = ThoughtNode(0, starting_user_input)
        self.current_idea = self.root #what node are we ideating off of?
        self.highest_id = 0
        self.depth = 0 #tracks response amount of conversation
        self.max_depth = max_depth 

    def parse_LLM(self, llm_response):
         # TODO: Parse response to find the delimiters "story #)" and attach to appropriate Node
        if self.depth == self.max_depth: #Max depth reached!
             print("Max Depth Reached! Returning Max Depth")
             return self.max_depth
        
        story_label = r'(story \d+:)'

        stories = re.split(story_label, llm_response, flags=re.IGNORECASE)
        stories = [story.strip() for story in stories if story.strip()]

        ## TODO: Remove the non relevant text before story 1) if it exists!

    
        for i in range(0, len(stories), 2):
            print(stories)
            story_label = stories[i]
            story_content = stories[i+1]
            pattern = r"(?i)\bstory\s+(\d+):"
            num = re.search(pattern, story_label)
            story = self.current_idea.add_child(int(num),story_content)
            if int(story.id) > self.highest_id:
                self.highest_id = int(story.id)
            

        self.depth +=1
        return self.depth
    
    def return_stories(self, user_response):
         # TODO: Return appropriate prompt (based on user_response) and attached stories to said prompt
        
        if self.depth == 0:
            return starting_prompt(user_response)

        story_label = r"story \s+\d+:" 
        matches = re.findall(story_label, user_response, re.IGNORECASE)

        thought_list = []
        for i in range(len(matches)):
            thought_list.append(self.__find_node_by_id(self.root,int(matches[i])))
        
        thought_list = [thought for thought in thought_list if thought is not None] #removing Nones

        if self.depth == self.max_depth:
            return finish_prompt(user_response,thought_list)

        if len(thought_list) >= 1: 
            self.current_idea = thought_list[0] #the first mentioned thought is the basis for new roots
            # TODO: Change this to reflect the critisism? (if talking about multiple stories, make trees appropriatly)

        c_prompt = critique_prompt(user_response, thought_list, self.highest_id)

        return c_prompt
    
    def __find_node_by_id(self, node, id):
        if node.id == id:
            return node
        
        for child in node.children:
            result = self.__find_node_by_id(child, id)
            if result is not None:
                return result
        
        return None

    

    

    

