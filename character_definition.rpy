####################
#----script.rpy----#
####################
# The script of the game goes in this file. I recommend splitting up the script into multiple files.
# The following file is what I use for initializing the Visual Novel setting, including Characters, Sprites, BGs, CGs, animations, and transforms.
# I then call another script file, script1.rpy 

# Also, anything with a # in front of it is a comment, and thus will not be interpreted by the engine when the game is executed.

##############################
#----CHARACTER DEFINITION----#
##############################

# Declare characters used by this game. The color argument colorizes the name of the character.
# Colors are in Hex code, using six characters after a # for definition.
# You can find different colors here. http://www.color-hex.com

define e = Character("Eileen")
define mc = Character('Main Character', color="#ffffff") #white naem text
define morgana = Character('Morgana', color="#000000") #black name text

# As you can see, you can use at least 1 letter, or two initials, or a full name for the character definition. I like to use two or three letters myself.

############################
#----SPECIAL CHARACTERS----#
############################

# Sometimes special "characters" are used in scripts to get different effects.
# To differentiate these characters I prefer to use only one letter for their definition.

#EXAMPLES:


#----NARRATOR----#
# This character serves as a delivery method for narrative. I often use the "NVL" kind of text box, as seen below.

define nvl = Character(None, kind=nvl)

# If I want a narrator without the NVL type of text box, I'd code it like this:

define n = Character(None)

#----GLOSSARY----#
#The following example is useful if you have a glossary. I will go into more detail on how to set up a glossary later.
define g = Character('Glossary', color="#ffffff")

#----UNKNOWN----#
# This character is one method of easily taking a new character, whose name is yet unknown, and having their name displayed as "???" until their name is revealed.

define u = Character('???', color="#ffffff")

# There is a more complex method of changing a character name as well.
# Step One: First you define a Dynamic Character.

define emily = DynamicCharacter("maid_name")

#Next, go to label start.

# The game starts here.

label start:

    # These display lines of dialogue in NVL narration mode.

    nvl "This line is displayed in NVL narration mode."

    nvl clear

    #Be sure to use "NVL CLEAR" function to clear the screen of previous nvl entries. 

    n "While this line is not."


    #Step Two: set "maid_name" variable to mean something early on in the game. Remember that you don't need to use it right away.
    $ maid_name = "Maid"

    # ''now'' the variable "maid_name" exists - it's only created when you set it.

    u "Hello?"

    emily "Hi there, I'm a Maid!"

    emily "By the way, my name is Emily."

    $ maid_name = "Emily"

    emily "I'ts very nice to meet you!"

    # Emily, formally known only as a Maid, is now known as Emily.

    return
