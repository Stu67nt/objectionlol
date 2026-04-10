init:
    transform flip:
        xzoom -1.0

default persistent.good_ending = False
default persistent.bad_ending = False

#creating bubbles
image holdit:
    "holdit.gif"
    size (1440, 1080)

image objection:
    "objection.gif"
    size (1440, 1080)


# creating backgrounds
image defence bg:
    "images/defence_bg.png"
    size (1440,1080)

image prosecution bg:
    "images/prosecution_bg.png"
    size (1440,1080)

image witness bg:
    "images/witness_bg.png"
    size (1440,1080)

# creating desks
image prosecution bench:
    "images/prosecution_bench.gif"
    size (1240 ,240)

image defence bench:
    "images/defence_bench.gif"
    size (1240 ,240)

image witness stand:
    "images/witness_stand.gif"
    size (1240 ,240)


# Creating pheonix and animations
define pheonix = Character("Pheonix Wright", color = "#ff0000")

image pheonix thinking:
    "images/pheonix/phoenix-thinking(a).gif"
    size (1440,1080)

image pheonix coffee:
    "images/pheonix/phoenix-coffee(a).gif"
    size (1440,1080)

image pheonix document:
    "images/pheonix/phoenix-document(a).gif"
    size (1440,1080)

image pheonix handsondesk:
    "images/pheonix/phoenix-handsondesk(a).gif"
    size (1440,1080)

image pheonix normal:
    "images/pheonix/phoenix-normal(b).gif"
    size (1440,1080)

image pheonix coffeed:
    "images/pheonix/phoenix-coffeed(b).gif"
    size (1440,1080)

image pheonix confident:
    "images/pheonix/phoenix-confident(b).gif"
    size (1440,1080)

image pheonix ohshit:
    "images/pheonix/phoenix-ohshit.gif"
    size (1440,1080)

image pheonix sweating:
    "images/pheonix/phoenix-sweating(b).gif"
    size (1440,1080)


# Creating edgeworth and animations
define edgeworth = Character("Edgeworth", color = "#ff0000")

image edgeworth thinking:
    "images/edgeworth/edgeworth-thinking(b).gif"
    size (1440,1080)

image edgeworth strained:
    "images/edgeworth/edgeworthDA-strained(b).gif"
    size (1440,1080)

image edgeworth pointing:
    "images/edgeworth/edgeworth-pointing(b).gif"
    size (1440,1080)

image edgeworth document:
    "images/edgeworth/edgeworth-document(b).gif"
    size (1440,1080)

image edgeworth confident:
    "images/edgeworth/edgeworth-confident(b).gif"
    size (1440,1080)


# Creating Godot and animations
define godot = Character("Godot", colour= "#ff0000")

image godot damage:
    "images/godot/godot-damage.gif"
    size (1440,1080)

image godot break:
    "images/godot/godot-break(b).gif"
    size (1440,1080)

image godot catch steaming:
    "images/godot/godot-catch steaming.gif"
    size (1440,1080)

image godot handondesk mug:
    "images/godot/godot-handondesk mug.gif"
    size (1440,1080)

image godot objection toss:
    "images/godot/godot-objection toss.gif"
    size (1440,1080)


# Creating Franziska and animations
define franziska = Character("Franziska", colour= "#ff0000")

image franziska damage:
    "images/franziska/franziska-damage.gif"
    size (1440,1080)

image franziska mad:
    "images/franziska/franziska-mad(a).gif"
    size (1440,1080)

image franziska tisk:
    "images/franziska/franziska-tisk(b).gif"
    size (1440,1080)

image franziska ready:
    "images/franziska/franziska-ready(b).gif"
    size (1440,1080)

image franziska clench:
    "images/franziska/franziska-clench(b).gif"
    size (1440,1080)

image franziska withwhip:
    "images/franziska/franziska-withwhip(b).gif"
    size (1440,1080)

image franziska ha:
    "images/franziska/franziska-ha(b).gif"
    size (1440,1080)


define apollo = Character("Apollo", color = "#ff0000")

image apollo normal:
    "images/apollo/apollo-normal(b).gif"
    size (1440,1080)

image apollo objects:
    "images/apollo/apollo-objects(b).gif"
    size (1440,1080)


# Creating Maya and animations
define maya = Character("Maya", colour= "#ff0000")

image maya thinking:
    "images/maya/maya-thinking(b).gif"
    size (1440,1080)

image maya mad:
    "images/maya/maya-mad(b).gif"
    size (1440,1080)


# The game starts here.
label start:
    play music "Court_Begins_-_Phoenix_Wright_-_Ace_Attorney_OST.mp3" loop
    scene prosecution bg
    show prosecution_bg
    show edgeworth thinking zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "Ok what is it"

    scene defence bg
    show defence_bg
    show pheonix thinking zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "77+33"

    scene prosecution bg
    show prosecution_bg
    show edgeworth thinking zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "well obviously it's"
    pause 0.4

    menu:
        "What is 77+33?"
        "77+33=100":
            show holdit at truecenter zorder 3
            play sound "Phoenix - Hold it.mp3"
            pause 1.4
            jump good
        "77+33=110":
            show holdit at truecenter zorder 3
            play sound "Phoenix - Hold it.mp3"
            pause 1.4
            jump bad


label bad:
    scene defence bg
    show defence_bg
    show pheonix coffee zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "77+33=110"

    scene prosecution bg
    show prosecution_bg
    show edgeworth thinking zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "Why mention that"
    pause 0.4

    scene defence bg
    show defence_bg
    show pheonix coffee zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "Oh nothing, i think the judge is comming back"

    if persistent.good_ending == False:
        "Please select the other option I put way more time into \nthat one. This is just for the requiement."

    $ persistent.bad_ending = True

    return

label good:
    scene defence bg
    show defence_bg
    show pheonix coffee zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "77+33=100"

    play music "Phoenix_Wright_Ace_Attorney_OST_-_Pressing_Pursuit__Cornered.mp3" loop

    scene prosecution bg
    show prosecution_bg
    show godot damage zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene prosecution bg
    show prosecution_bg
    show edgeworth strained at flip zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene prosecution bg
    show prosecution_bg
    show franziska damage zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene witness bg
    show witness_bg
    show maya thinking zorder 1:
        yoffset 20
    show witness stand zorder 2
    maya "I think it's 2"

    scene prosecution bg
    show prosecution_bg
    show godot damage zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene prosecution bg
    show prosecution_bg
    show edgeworth strained at flip zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene prosecution bg
    show prosecution_bg
    show franziska damage zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene defence bg
    show defence_bg
    show pheonix thinking zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "Wait lemme pull out this random analysis I found on the floor"

    scene prosecution bg
    show prosecution_bg
    show franziska mad zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    franziska "u cant just do that!1!11!!1"

    scene defence bg
    show defence_bg
    show pheonix document zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "If 7+3=10, how is 77+33 not 100?"

    show pheonix handsondesk
    pheonix "Explain"

    scene prosecution bg
    show prosecution_bg
    show edgeworth strained at flip zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene prosecution bg
    show prosecution_bg
    show godot break zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    "*dies*"

    scene prosecution bg
    show prosecution_bg
    show franziska tisk zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    franziska "allow me to grab this random analysis in the floor"

    scene defence bg
    show defence_bg
    show pheonix handsondesk zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "THAT DOESNT MAKE ANY SENSE"

    scene prosecution bg
    show prosecution_bg
    show franziska ready zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    franziska "no one cares 77+33=99"

    scene prosecution bg
    show prosecution_bg
    show godot break zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    "*dies* x2"

    scene prosecution bg
    show prosecution_bg
    show edgeworth thinking zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "can we chill out for a sec my pizza is melting"

    scene defence bg
    show defence_bg
    show pheonix coffee zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "no"

    scene prosecution bg
    show prosecution_bg
    show edgeworth strained at flip zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "Explain that god forsaken analysis of yours then"

    scene defence bg
    show defence_bg
    show pheonix coffee zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "no"

    scene prosecution bg
    show prosecution_bg
    show godot catch steaming zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    godot "Man's stupider than my dog squared"

    scene prosecution bg
    show prosecution_bg
    show edgeworth pointing zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "77+33=110"

    scene defence bg
    show defence_bg
    show pheonix coffee zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "no"

    scene prosecution bg
    show prosecution_bg
    show edgeworth strained at flip zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "God save me"

    scene witness bg
    show witness_bg
    show maya thinking zorder 1:
        yoffset 20
    show witness stand zorder 2
    stop music
    play music "Phoenix_Wright_Ace_Attorney_OST_-_Maya_Fey__Turnabout_Sisters_Theme_2001.mp3" loop
    maya "can we stop arguing"

    scene defence bg
    show defence_bg
    show pheonix normal zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "ok"

    scene prosecution bg
    show prosecution_bg
    show edgeworth thinking zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "ok"

    scene prosecution bg
    show prosecution_bg
    show franziska clench zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    stop music
    play music "Court_Begins_-_Phoenix_Wright_-_Ace_Attorney_OST.mp3" loop
    franziska "ok we do the thing now"

    scene prosecution bg
    show prosecution_bg
    show edgeworth document zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "70+30 is 100, is it not?"

    scene defence bg
    show defence_bg
    show pheonix thinking zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "no"

    scene prosecution bg
    show prosecution_bg
    show godot break zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    godot "why you do this to me"

    scene prosecution bg
    show prosecution_bg
    show franziska ready zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    franziska "i guess it is idrk i suck at maths"

    scene prosecution bg
    show prosecution_bg
    show edgeworth pointing zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "7+3=10 is it not?"

    scene defence bg
    show defence_bg
    show apollo normal zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    apollo "Yo what's going on?"

    scene prosecution bg
    show prosecution_bg
    show edgeworth pointing zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "Do you know how much 77+33 is?"

    scene defence bg
    show defence_bg
    show apollo objects zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    apollo "It's 100"

    stop music
    play music "Phoenix_Wright_Ace_Attorney_OST_-_Pressing_Pursuit__Cornered.mp3" loop
    scene prosecution bg
    show prosecution_bg
    show edgeworth strained at flip zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "God damn"

    scene prosecution bg
    show prosecution_bg
    show franziska withwhip zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    franziska "apollo what the hell"

    scene defence bg
    show defence_bg
    show pheonix normal zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "Apollo you genius"

    scene prosecution bg
    show prosecution_bg
    show godot objection toss zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    godot "Shut the hell up"

    "Godot threw a mug but the animation \nbudget was 0 so no actual annimation"

    scene defence bg
    show defence_bg
    show pheonix coffeed zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "...continue edgeworth"

    scene prosecution bg
    show prosecution_bg
    show edgeworth pointing zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "As I was saying 7+3=10, is it not?"

    scene defence bg
    show defence_bg
    show apollo objects zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    apollo "NO"

    scene prosecution bg
    show prosecution_bg
    show godot objection toss zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    godot "GET OUTTTTT"

    "In a blind fit of rage, Godot threw 5 mugs at Apollo"

    scene prosecution bg
    show prosecution_bg
    show edgeworth pointing zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    godot "100+10=110"

    scene defence bg
    show defence_bg
    show pheonix confident zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "WHERE DID YOU GET THOSE NUMBERS FROM"

    scene prosecution bg
    show prosecution_bg
    show edgeworth pointing zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    godot "70+30 is 100, 7+3 is 10 and how much is 100+10?"

    scene prosecution bg
    show prosecution_bg
    show franziska ha zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    franziska "It's 99"

    show objection at truecenter zorder 3
    play sound "Phoenix - objection.mp3"
    pause 1.5

    scene defence bg
    show defence_bg
    show pheonix confident zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "66+33=99"

    stop music
    play music "Phoenix_Wright_-_Trials_and_Tribulations_OST_-_Pressing_Pursuit__Caught.mp3" loop
    scene prosecution bg
    show prosecution_bg
    show edgeworth confident zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    godot "Congratulations on being smart for the first time"


    scene prosecution bg
    show prosecution_bg
    show franziska ha zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    franziska "66+44=100"

    scene prosecution bg
    show prosecution_bg
    show godot handondesk mug zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    godot "I disagree"

    scene prosecution bg
    show prosecution_bg
    show edgeworth document zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "66+44 and 77+33 have the same value"

    show edgeworth confident zorder 1:
        yoffset 20
    edgeworth "So by that logic, 77+33 is 110"

    scene defence bg
    show defence_bg
    show pheonix thinking zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "How much is 66+44"

    scene prosecution bg
    show prosecution_bg
    show edgeworth thinking zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "same as 77+33 value"

    scene defence bg
    show defence_bg
    show pheonix confident zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "So it's 100?"

    scene prosecution bg
    show prosecution_bg
    show godot damage zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene prosecution bg
    show prosecution_bg
    show edgeworth strained at flip zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene prosecution bg
    show prosecution_bg
    show franziska damage zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    pause 0.4

    scene prosecution bg
    show prosecution_bg
    show godot catch steaming zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    godot "It's 110"

    scene prosecution bg
    show prosecution_bg
    show edgeworth pointing zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "It's 110 it's so obvious"

    scene defence bg
    show defence_bg
    show pheonix document zorder 1:
        yoffset 20
    show defence bench zorder 2:
        xoffset -200
    pheonix "Wait let me do the math"

    show pheonix ohshit zorder 1:
        yoffset 20
    pause 0.5

    show pheonix sweating zorder 1:
        yoffset 20
    pheonix "...why do I suck at maths"

    scene prosecution bg
    show prosecution_bg
    show franziska tisk zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    franziska "see im better than u in maths haha"

    # Add holdit sound
    show holdit at truecenter zorder 3
    play sound "Phoenix - Hold it.mp3"
    pause 1.4

    scene prosecution bg
    show prosecution_bg
    show edgeworth confident zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "You are trash at maths"

    scene prosecution bg
    show prosecution_bg
    show franziska withwhip zorder 1:
        yoffset 20
    show prosecution bench zorder 2:
        xoffset 200
    edgeworth "i hate u"

    if persistent.bad_ending == False:
        "Try the other option or don't idk im not ur mum."

    $ persistent.good_ending = True

    return