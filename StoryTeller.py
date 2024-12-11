from MAD.MADprompts import *
from MAD.MADstruct import *
from ToT.TreeofThoughts import *
import argparse
import sys

parser = argparse.ArgumentParser(description="Use the following flags to customize StoryTeller")

parser.add_argument(
    '--story', 
    type=str, 
    default = None,
    help="Path to the input .txt file. If not input, then story idea will be provided by the user"
    )
parser.add_argument(
    '--human', 
    action='store_true', 
    help= "If input is true, then story feedback in Tree of Thoughts is done by human input, rather than semi-random criticism"
)
parser.add_argument(
    '--depth', 
    type=int, 
    default=2, 
    help="Number for depth for the Tree of Thoughts. Default is 2."
)
parser.add_argument(
    '--rounds', 
    type=int, 
    default=2, 
    help="Number for rounds for MAD between Proponent and Opponent. Default is 2."
)

args = parser.parse_args()


story_string = None

# Validate story file +                                                                                                          
if args.story is not None:
    if not args.story.endswith('.txt'):
        print("Error: File must have a .txt")
        sys.exit(1)
    try:
        with open(args.story, 'r') as file:  
            story_string = file.read()  
    except FileNotFoundError:
        print(f"Error: File not found at {args.story}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


# This file includes the ToT-to-MAD pipeline
# Initialize chat history
proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history = initialize_chat_history()
print("Author:", story_intro_prompt())


# Can implement ToT here and get a result to feed into MAD 
ToT_result = ToTloop(given_story = story_string, human_response= args.human, max_depth = args.depth)


# Can leave ToT_result as None if want to run MAD loop by itself
MAD_loop(ToT_result, proponent_chat_history, moderator_chat_history, opponent_chat_history, author_chat_history, args.rounds)