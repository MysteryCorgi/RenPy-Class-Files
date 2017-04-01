####################
#----script.rpy----#
####################
# The script of the game goes in this file. I recommend splitting up the script into multiple files.
# The following file is what I use for initializing the Visual Novel setting, including Characters, Sprites, BGs, CGs, animations, and transforms.
# I then call another script file, script1.rpy to insert the game's main story code. I often break it up into several script files. script2.rpy and onwards.
# The longest script I've had was from script.rpy to script10.rpy


#######################
#-------SPRITES-------#
#######################

# Sprites are the images that represent the characters defined in the text.
# Generally, .PNG files are used for basic sprites, as they are files that can have transparency.

#A Basic sprite definition follows this format:
# image character expression = "images/SPR/character_expression.png"

# For example:

# Morgana Normal Outfit
image morgana neutral = "images/SPR/Morgana/morgana_neutral.png"
image morgana smile = "images/SPR/Morgana/morgana_smile.png"

# However, you may have an alternate outfit or version of a character:

#Morgana Dress1 Outfit
image morgana dress1 neutral = "images/SPR/Morgana/Dress1/morgana_dress1_neutral.png"

# This would show the character Morgana in a dress as opposed to her normal outfit.

###########################
#----BACKGROUND IMAGES----#
###########################

# A background image is like the stage on which your character stands. It is the setting of your scene.

 #A simple background would be the color black. Which is easy to code!

image black = "#000"


# However black is the only color you can use a hex color code for as a background. For any others you'll have to make an image.
# For Example:

image white = "images/BGS/white.png"


#However, plain old colors would be boring! So let's try an actual image for a background.

#image grass_field = "images/BGS/Grass_Field/grass_field.png"

# Alternatively you can have variations on a background. This can show you times of day and such.

#image grass_field morning = "images/BGS/Grass_Field/grass_field_morning.png"
#image grass_field evening = "images/BGS/Grass_Field/grass_field_evening.png"



####CLEARING AFTERNOON####
# If you want to animate a background, here is an example of how to do so.
image clearing_afternoon_base = "images/BGS/Clearing_Afternoon/clearing_base.png"
image grass_01 = "images/BGS/Clearing_Afternoon/grass_01.png"
image grass_02 = "images/BGS/Clearing_Afternoon/grass_02.png"
image grass_03 = "images/BGS/Clearing_Afternoon/grass_03.png"


image clearing_grass:
    contains:
        "grass_01"
        pause 0.20
        "grass_02"
        pause 0.20
        "grass_03"
        pause 0.20
        "grass_02"
        pause 0.20
        "grass_01"
        pause 0.20
        "grass_02"
        pause 0.20
        "grass_03"
        pause 0.20
        "grass_02"
        pause 0.20
        "grass_01"
        pause 0.20
        "grass_02"
        pause 0.20
        "grass_03"
        pause 0.20
        "grass_02"
        pause 0.20
        repeat
        
image clearing_afternoon:
    subpixel True
    contains:
        xalign 0.0
        yalign 0.0
        "clearing_afternoon_base"
    contains:
        xalign 0.0
        yalign 0.0
        "clearing_grass"


###########################
#----CUSTOM TRANSFORMS----#
###########################

# You can use custom transforms to change how your characters appear, move, and act on screen. 


#----BOUNCE----#
# The following allows characters to "bounce" once.
init:
    transform bounce:
        linear 0.2 xoffset 0 yoffset 14
        linear 0.2 xoffset 0 yoffset 0


# The following allows a character to be shown or hidden with a fade.
    transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 1.0 alpha 0.0  

# The following flips a character to face the opposite direction.
    transform flip:
        xzoom -1

# The following positions a character between the left and center of the screen.
    transform centerleft:
        xalign 0.25
        yanchor 1.0
        ypos 1.0
 
 # The following positions a character between the center and rigth of the screen.       
    transform centerright:
        xpos 0.65
        yanchor 1.0
        ypos 1.0




# The game starts here.

label start:

    # set the scene to black

    scene black

    # Set the scene to show a background

    scene clearing_afternoon

    # Introduce a character sprite at custom transform location with basic fade transform, and flipped.

    show morgana neutral at centerleft, basicfade

    "Ah what a beautiful field!"

    show morgana neutral at flip
    "Let's look around!"

    # move character to centerleft and  moving in from the right

    show morgana smile at centerright with moveinleft

    "I'm over here now!"



    return
