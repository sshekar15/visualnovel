# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elle")
define c = Character("Ryan")
define s = Character("Sarah")
define k = Character("Chris")
define u1 = Character("Unknown girl 1")
define u2 = Character("Unknown girl 2")
define p = Character("[player_name]", color="#6d43df")
init:
    $ affection_elle = 0
    $ affection_ryan = 0
    $ affection_sarah= 0
    $ affection_chris = 0
init python:
    import random

    # List of possible killers (names should match your character IDs)
    suspects = [e,c,s,k]

    # Randomly select the killer
    killer = random.choice(suspects)

# The game starts here.

label start:
    scene 1
    "Welcome to Highschool"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    scene start
    # Now use the player's name in the dialogue

    e "Hi. You must be the transfer student."

    e "What's your name?"
    $ player_name = renpy.input("Enter name:")  # Prompt to input name
    $ player_name = player_name.strip()  # Remove any extra spaces from the input

    if player_name == "John":  # Default name if no name is entered
        $ player_name = "Player"

    e "Welcome to Esa High,[player_name]. I'm Elaine, you can call me Elle. I'll be your Guide."

    e "Let's head to your first class."

    scene firstmeet

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    e "This is your first class! Do you have any questions for me?"

    menu:
        "Ask about the school":
            e "Well, it's a great school! We have lots of clubs, and the teachers are nice."
            scene defaultinclass
            e "Are you curious about the rumors? Is that why your asking?"
            menu: 
                "What rumors?":
                    scene firstmeet
                    $ affection_elle += 5
                    e "Don't worry about it! You just joined."
                "Yeah. They are pretty weird.":
                    $ affection_elle -= 5
                    scene sadorstrictinclass
                    e "This isn't the best time to discuss that. For now keep your head down."
            
        "Ask about her":
            e "Oh, me? I’m just a student here too."

            e "I'm class president too. So if you need help I'll be there."
            menu:
                "Thanks.":
                    scene flushedinclass
                    $ affection_elle += 5 
                    e "No problem."
                "I don't need your help.":
                    scene angryinclass
                    e "Whatever. You won't even make it a day like the other tranfer student anyway."

    "Elle's trust points: [affection_elle]"
    scene defaultinclass
    e "Anyway I got to go to class now. Be careful."

    scene smp_classroom1_day2

    "After a hour. You can't stop thinking about what Elle meant about rumors."

    "She had told you to {i}be careful{/i}. Why would she tell you that?"

    scene smp_classroom2_day2

    "As you're leaving the class you bump into someone."

    "Ouch!"
    
    scene defaultinclassry

    c "Watch where you're going!"

    menu:
        "{i}You{/i} bumped into me!":
            $ affection_ryan -= 5 
            scene angryinclassry
            c "You're the one not looking where you're going."

        "Sorry.":
            $ affection_ryan += 5 
            c "Whatever."
    c "Wait. I know you. You're the new transfer student. What was your name again? It's [player_name] right?"
    scene defaultinclassry

    menu:
        "Yes? Have we met before?":
            c "Nah. You're just brave coming here after what happened to the last transfer."

            menu:
                "What happened?":
                    c "You don't know?"

                    c "They died."
                "I don't listen to rumors.":
                    scene happyinclassry
                    c "He laughs."
                    scene defaultinclassry

                    c "If I were you, I would."

                    c "After all they died."
    menu: 
        "How?":
            c "They jumped off the roof. But rumors say that they were pushed.."
        "What happened?":
            c "No idea. There are rumors though: that they were killed."

    c "I can't tell you any more. If you're curious listen to the gossip."

    menu:
        "Thanks.":
            scene happyinclassry
            $ affection_ryan += 5 
            c "Just being a good citizen. Be careful."
        "I don't care.":
            $ affection_ryan -= 5 
            scene angryinclassry
            "Scoff"

            c "Just watch your back, kid."
    "He leaves."
    "Ryans's trust points: [affection_ryan]"

    "He seems to be odd. He was unfazed about someone's death like it was nothing."

    scene emptyclass
        
    "Rumors again. What could have happened in this school?"

    s "Don't worry about it. Ryan is always like that."

    "You turn and see a girl."

    scene defaultinclasssarah

    s "I'm Sarah. The class vice president."

    menu:
        "You are? Elle didn't mention you.":
            $ affection_sarah -= 5
            s "She probably forgot."
        "Nice to meet you.":
            $ affection_sarah += 5
            s "You too."
    "Since she is here maybe you can finally understand what this rumor is about, and if it was true."

    menu:
        "Ryan mentioned rumors. Are they true?":
            s "No way. Someone did die but it wasn't murder."

            menu:
                "I never mentioned it was murder.":
                    $ affection_sarah -= 5
                    s "I've already heard the rumors before."

                "How sure are you?":
                    $ affection_sarah += 5
                    "She hesiates then shakes her head."

                    s "There is no way it was murder."

        "Ryan said that a transfer student died. Is that true?":
            s "Sigh"
            s "Yeah. A student did die."

        "Who killed the other transfer student?":
            s "Killed? They jumped off the roof themself."

    s "She shakes her head."

    s "Don't worry about it. Anyway head to your next class."
    "Sarah's trust points: [affection_sarah]"

    scene emptyclass

    "You try to shake of your unease and leave."

    scene clubempty

    "You head to a random club and find a blue haired boy painting."

    scene suprisedclubchris

    "He looked up at you suprised before smiling."
    
    scene happyclubchris

    k "Hi. You must be [player_name]. I'm Chris."

    menu:
        "Yeah. Is that your painting? It looks good.":
            $ affection_chris += 5
            "He nods."
            k "Thanks!"
        "Yeah. What club is this?":
            $ affection_chris -= 5
            k "Art club."
            k "So? Are you intrested in joining?"
            menu:
                "Yes.":
                    k "That's great!"

                "No.":
                    k "That's fine."
    scene defaultclubchris

    "He seems nice. Maybe you could try to ask him more about the rumors."
    menu:
        "Do you know about the rumors?":

            scene suprisedclubchris

            k "Yeah."
            scene sadclubchris

            "He looks a bit uneasy. That's odd."
            menu:
                "Do you belive in it?":
                    $ affection_chris += 5
                    scene sadclubchris
                    "He looks hesitant and shakes his head."

                    k "Of course not."

                "Is it true?":
                    $ affection_chris -= 5
                    scene sadclubchris
                    "He pauses like he is thinking."

                    k "Someone did die but..."

                    k "It wasn't murder."

                    "The way he said it was a bit odd."

    "He gathers his stuff."

    scene defaultclubchris

    k "Sorry, I have to go to class."

    "Chris's trust points: [affection_chris]"

    scene clubempty

    "You watch him leave. As he leaves you see a dark red stain on his bag. Was it paint?"

    scene emptyclass

    "You head back to class thinking about the werid encounters you've had. You know for sure someone died here, but why and was it murder?"

    scene emptyclassafternoon

    "After a few hours. You come across a group of students gossiping."

    "You hear them whispering about something and hear your name so you listen in."

    u1 "Did you hear about the new transfer [player_name]?"

    u2 "Yeah. I saw them talking to Elle, Ryan, Sarah and Chris today."

    u1 "Isn't that the 4 students suspected for the other transfer's death?"

    u2 "Yeah. I heard the cops saying how all four were the top suspects."

    "They were? No wonder they all tried to aviod the topic."

    label investigation_menu:
        scene emptyclassafternoon

        "Maybe you should investigate. Where should you start?"

        menu:
            "Investigate the classroom. Info about Ryan.":
                jump investigate_classroom

            "Investigate the office. Info about Elle and Sarah.":
                jump investigate_office

            "Investigate the art club. Info about Chris.":
                jump investigate_artclub

            "You've seen all you need to see. You've made your descision.":
                jump investigation_end

    label investigate_classroom:

        scene classroomeve
        "You sneak back into the classroom Ryan was in earlier."

        "You dig around in the teacher's drawer and find a few confiscated items."

        scene emptyclassthreat

        "One stands out: a folded note with Ryan’s name written in sloppy handwriting."

        "You open it carefully."

        "\"If you keep threatening me, I'll go to the principal. I'm not scared of you anymore.\""

        $ evidence3 = "Threat note to Ryan"

        "It's unsigned, but the date matches just days before the transfer student's death."

        "Did Ryan have something over them? Did they fight?"

        "Then, you find a torn corner of a disciplinary form with Ryan’s name… and the word 'roof' partially visible."

        scene emptyclassformnew

        $ evidence4 = "Partial disciplinary form"

        "Why would Ryan be warned about the roof? What happened up there?"

        jump investigation_menu

    label investigate_office:

        scene officeeve
        "You sneak into the school office. You hope to find something about Elle or Sarah."

        "You find a stack of incident reports."

        "One catches your eye. It’s dated just a week before the previous transfer student died."

        "It’s a complaint form... Filed {i}against{/i} Elle. By the transfer student."
        scene officecomelle

        $ evidence = "Complaint against Elle"

        "It says Elle was pressuring them to quit a school club. Apparently, Elle said they were 'ruining things.'"

        "You scan it and your eyes widen — the previous transfer student had been nominated to replace Elle as class president."

        "They had gained a lot of support quickly. It would’ve meant Elle losing her position."

        $ motive_elle = "Transfer student almost took her class president spot"
        scene officeevn

        "You also find a sealed envelope marked 'Confidential – Academic Integrity Committee.'"

        "You open it carefully. Inside is a case file on Sarah."
        scene officecom

        "The document includes allegations that Sarah {i}cheated on her college entrance exam{/i} — reported anonymously."

        "The witness? The transfer student."

        "There’s an official school notice attached:"

        "\"Testimony scheduled for Thursday morning – Student: Name Redacted.\""

        "You glance at the date. The transfer student died {i}the day before{/i} the hearing."

        "With no witness, the accusation was dropped and marked as 'unsubstantiated.'"

        $ motive_sarah = "Transfer student was going to testify about Sarah’s cheating but died the day before"

        scene officeeve

        "Sarah had everything to lose. College. Reputation. Her future."

        "Two strong motives. Two suspects trying to protect what mattered most."

        jump investigation_menu

    label investigate_artclub:

        scene nightatclub
        "You quietly enter the dark art clubroom."

        "Paintings line the walls. The room smells like turpentine... and something else."

        "You find Chris’s corner. His sketchpad is left behind."

        "You flip through — most are normal... until one catches your eye."

        "A drawing of someone standing at the edge of the school roof, surrounded by dark shadows."

        $ evidence5 = "Chris’s sketch of rooftop scene"

        "It’s eerie. The person drawn looks terrified. The eyes are familiar..."

        "You turn the page and see a poem written messily beside it."
        scene clubpoem

        "\"Crimson silence stains the sky,
            Secrets spill where angels die.
            A step, a scream — the air was thin,
            I watched the fall. I kept it in.\""

        $ evidence6 = "Chris’s poem"

        "Was Chris a witness? Or was this guilt?"

        "Then you spot his bag in the corner. The red stain is still there."

        "You sniff it. It doesn’t smell like paint."

        jump investigation_menu

    label investigation_end:

        scene emptyclassafternoon
        "Armed with new evidence, your mind races."

        "Everyone had a motive. Everyone had secrets."

        "Now it’s up to you to decide: Who is lying, and who is dangerous?"

        # Placeholder — Jump to confrontation scene or final decision
    scene fronteve

    "Since it's so late you decide to go home and think more."

    scene 1

    "You enter school early the next day."

    scene emptyclass

    "You enter the classroom and overhear whsipers. You recognize the voices. It's the four students from yesterday. The four top suspects of the last transfer student's death. "


    e "The new transfer. I heard they were curious. What did you tell them?"

    c "Scoffs"

    c "I told them nothing blondie."

    s "Someone broke into office and classroom yesterday."

    k "Do you think they know?"

    "You decide to interrupt and confront them."

    menu: 
        "I do.":
            "They all look suprised at your presence."
    scene allclass
    label confrontation:
        
        "They all turn to face you."

        p "I know one of you is lying."

        menu:
            "Accuse Elle":
                $ accused = e
                scene allclasselle
            "Accuse Ryan":
                $ accused = c
                scene allclassryan
            "Accuse Sarah":
                $ accused = s
                scene allclasssarah
            "Accuse Chris":
                $ accused = k
                scene allclasschris

    if accused == killer:
        killer "..."
        killer "So you figured it out."

        killer "I didn't mean for it to happen. But they left me no choice."

        "The others step back in shock. You’ve done it."

        "You exposed the killer."

        "You had in the evidence and the killer is caught by the cops."

        jump good_ending

    else:
        accused "What? You think I did it? You're wrong!"

        if killer == e and affection_elle < 10:
            jump bad_ending
        elif killer == c and affection_ryan < 10:
            jump bad_ending
        elif killer == s and affection_sarah < 10:
            jump bad_ending
        elif killer == k and affection_chris < 10:
            jump bad_ending
        else:
            killer "You're lucky I like you, [player_name]."

            killer "But next time, choose your words more carefully."

            "You feel a chill run down your spine."

            jump spared_ending

    label good_ending:
        scene 1
        "The killer is taken away by the authorities."

        "Justice is served. You've uncovered the truth."

        return

    label bad_ending:
        scene black
        "Suddenly, everything goes dark."

        "You never make it out of the school that night..."

        return

    label spared_ending:
        scene 1
        "You survived — barely. But you know the truth now."

        "The killer is still out there. Watching."

        return




    


        



    




            




    # This ends the game.

    return
