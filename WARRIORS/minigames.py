# PLAY AS A CHARACTER WHICH MUST FIND ALLIES ALONG THE QUEST AND DEFEAT THE DARK LOREM. 
# YOU CHOOSE A CHARACTER TO START WITH, EACH CHARACTER IN THE GAME HAS THEIR OWN SUPERPOWERS/ABILITIES.

# CHARACTERS
from characters import Character

# FADE, JAZOK, BRUTE, DANCIV, AKOLLA, ZUOKA, PVISKI, JOSEV, MANDALTAN, SJOLKOO, GOROX, SLATTER, ENDERWITCH, MAYSON

# ATTRIBUTES
# ATTACKS, CONVINCING, MAGIC, DEFENCE, FREEZING, TIME, WATER, SOUL, ENERGY, HUNGER, 


# GAMEPLAY:
# [YOU AND GOTROX BUMPS TO EACH OTHER AND GOROX TURNS]
# GOROX: HEY WATCH WHERE YOU ARE GOING.


# STORY AS A WHOLE IS MADE WITH MANY STORY LINES FORMING A LARGE TREE
# A STORYLINE CAN BE A STORY TO CHILDREN STORYLINES

from stories import Story

# -------------------------------------------------------------------------------------------------------------------------------------
# INTRODUCTION
# -------------------------------------------------------------------------------------------------------------------------------------
Intro = Story("""
Once apon a time. In a town where peace was the way of life, there once existed a king named Osolnas. King Osolnas was the 
greatest king they could ever ask for. He took care of his people like he was taking care of himself. King Osolnas then died a few 
years after leading his people... let's say two years. This was quite a short time to live. Long live King Osolnas. This is where you
come in, you as [characted] have received a letter from Anonymous. They seem to have information about who killed the king. This was
very shocking to hear thet the king of "[the land of magic]" has been killed by an insider. You are the only one who knows about this
letter.
THIS IS WHERE IT ALL BEGANS...""")
Intro.add_storylines({"1": "Inform the king [King Javax]", "2": "Read the letter again", "3": "Head to meet with Anonymous", 
                      "4": "Don't care"})


# -------------------------------------------------------------------------------------------------------------------------------------
# INFORM THE KING
# -------------------------------------------------------------------------------------------------------------------------------------
InformTheKing = Story("""
You are on your way to King Javax about this....
As you start approching the castle you see two people standing in the way. They look like they are waiting for you to approach them. You
fold the letter and put it in your packet as you approach them. They seem like Elobie warriors
HINT: TYPE THE COMMAND "HELP(INFO ABOUT ELOBIE WARRIOURS)" IF YOU WANT TO KNOW MORE ABOUT THESE WARRIOURS

A tall skinny guy from these warriors comes forward from these warriours.
[THOUGHTS]: "Huh. This may be their leader.. what do they want from me."
          
UNAMED(tall skinny warrior): Greetings my friend. I am here to collect what i have sent you earlier. It was suppose to go to the other 
nation not this one. We apologise for the misunderstanding we have caused. You must be confused!
""")
InformTheKing.add_storylines({"1": "I think this belongs to the king not you!", "2": "Who are you and where do you come from?",
                             "3": "Why should i give you this?", "4": "[Don't say anything, Just look at him]"})


# -------------------------------------------------------------------------------------------------------------------------------------
# READ THE LETTER AGAIN
# -------------------------------------------------------------------------------------------------------------------------------------
ReadLetterAgain = Story("""
                                                                                                                        22 April 1805

I hope you are doing well my friend. I have heared you are looking for justice after what happened to our graceful king, King Osolnas.
We live in a world of hunger, so i will not waste your time and get straight to the point. I know who killed the king. I am willing to 
come clean as long as i will get something out of it. 22 golds, 22 Wolf leathers and 700 pennies of Oz. I am looking forward to seeing you
sir. Meet me at the Affel bridge tonign at night when you mean bussiness. Don't try anything funny!

Yours:
King Anonymous
""")
ReadLetterAgain.add_storylines({"1": "Wied! let me just ignore this", "2": "I have to report this to the king!", 
    "3": "[Check inventory..]", "4": "I'll go without all these demands.. I have to catcht that bastard!"})


# -------------------------------------------------------------------------------------------------------------------------------------
# HEAD TO MEET WITH ANONYMOUS
# -------------------------------------------------------------------------------------------------------------------------------------
MeetAnonymous = Story("""
[YOU DECIDED TO JUST ATTEND THIS IMMEDIATELY AND GO TO MEET ANONYMOUS!] YOU HAVE ARRIVED AT THE BRIDGE AND SEE A MAN COVERING HIS FACE WITH
A MASK.
                      
Anonymous: Let me first put you in the test. Lets duel. You win i tell you the story. I win i get to keep one of your abilities!
""")
MeetAnonymous.add_storylines({"1": "How is that possible", "2": "You cannot win against me.", "3": "That's too harsh. I cannot risk like that",
"4": "[Run Away..]"})


# -------------------------------------------------------------------------------------------------------------------------------------
# Reply to anonymous: You can't win against me.
# -------------------------------------------------------------------------------------------------------------------------------------
LetsDuel = Story("""
OK. WE'LL SEE ABOUT THAT! [GETTING READY TO DUEL.]

HINT: TYPE "HELP(DUEL)" TO SEE INSTRUCTIONS ON HOW TO DUEL. OR START RIGHT AWAY IF YOU KNOW HOW!

Anonymous: You will be starting.. I'm giving you advantage.
""")
LetsDuel
# -------------------------------------------------------------------------------------------------------------------------------------

# Branchings
Intro.branch({"1": InformTheKing, "2": ReadLetterAgain})
ReadLetterAgain.branch({"2": InformTheKing})
    
# tell story
Intro.tell()