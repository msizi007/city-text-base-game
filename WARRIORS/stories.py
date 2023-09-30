# AUTHOR: M.S.MWELASE
"""
# ARE YOU MAKING A TEXT BASED RPG OR WHATEVER AND TIRED OF REPEITING YOURSELF AND BRANCHING EVERYTHING TOGETHER? STORIES GOT YOU!
# THIS MODULE HAS FEW BASEC METHODS THAT JUST WORKS AS SMOOTH AS RECURSION (RERSURSIVE-LIKE).

# STORY <=> THIS IS A STORY BEING TOLD.
# STORYLINE <=> PATHS A STORY TAKES TO FORM A NEW STORY.

Main = Story("Where do you wanna go to?")
Main.add_storylines({"1": "go to the mall", "2": "walk home", "3": "quit game"}, "::> ")

MallScene = Story("The mall was fun, where do you wanna go now?")
MallScene.add_storylines({"1": "go home", "2": "exit"}, "::> ")

Main.branch({"1": MallScene})
Main.tell("::> ")
"""

class StoryLineError(Exception):
    def __Init__(self, message):
        super().__init__(message)

class Story:
    "tell a story you wanna create then use the .add_storylines to add storylines then brench them after and finnally tell the story to the world"
    def __init__(self, story: str):
        self.story = story
        self.storylines = dict()
        self.separators = None
        self.branch_stories = None

    def add_storylines(self, storylines: dict, separators: str="::> "):
        "add options to the story and their responses, and please provide keys as strings {'option': 'storyline'}"
        self.storylines = storylines
        self.separators = separators

    def branch(self, stories: dict):
        "method for adding more stories in the "
        self.branch_stories = stories

    def tell(self, prompt_string: str="::> "):
        "method to tell a new story and prompt user with a prompt_string"
        print(self.story)
        for opt, storyline in self.storylines.items():
            print(f"{opt} \t{self.separators}{storyline}")
            
        option = input(prompt_string)

        if self.branch_stories:
            if option in list(self.branch_stories.keys()):
                self.branch_stories.get(option).tell(prompt_string)
        else:
            raise StoryLineError("Storylines missing.. Story has reached conclusion.")



