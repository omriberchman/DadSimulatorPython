#                                                                   ~~~~ CREATED BY OMRI ~~~~
import os
import webbrowser
insert = "Insert your answer [IN NUMBERS!] : "
died , left, = "\n~~~~~~~~~~~~~ \n~~YOU DIED!~~ \n~~~~~~~~~~~~~\n" , "\n~~~~~~~~~~~~~~~~~~~~~~~~~~ \n~~You've been abandoned!~~ \n~~~~~~~~~~~~~~~~~~~~~~~~~~\n",

print("00000000000000000000000000000000000000000000000")
print("0000000000000000 Dad Simulator 0000000000000000")
print("00000000000000000000000000000000000000000000000")
print("\n\nChoose your dad : ")
print("\n1. Normal dad \n\n2. Asian dad \n\n3. Irresponsible dad\n")
dad = input(insert)
if dad == "1":
    print('')
    print("Good'ay son!")
    print("")
    print('How was school today?')
    print('1. Excellent, had a very informative day!')
    print('2. It was ok, not something special.')
    print('3. meh.. it was pretty boring...')
    answer1 = input(insert)

    if answer1 == '1':

        print('')
        print('')
        print("Why so?")
        print("1. I got A+ in test")
        print("2. We had an interesting lecture.")
        print("3. I got a kiss!")
        if1 = input(insert)
        if if1 == "1":
            print("Very good son.")
            print("In which subject was the test?")
            print("1. Math")
            print("2. PE")
            print("3.Physics")
            if11 = input(insert)
            if if11 == "1":
                print("Alright, you can go play some Ybox or whatever it is that you youngsters do.")
                print("~" * 33)
                print("~" * 6 + "Congrats YOU WON!!!1!" + "~" * 6)
                print("~" * 33)
            elif if11 == "2":
                print("Oh, That's sucks! You're a failure! Go and learn some math!")
                print(died)
                os.system('pause')
                exit()
            elif if11 == "3":
                print("Alright, you can go play some Ybox or whatever it is that you youngsters do.")
                print("~" * 33)
                print("~" * 6 + "Congrats YOU WON!!!1!" + "~" * 6)
                print("~" * 33)
        elif if1 == "2":
            print('')
            print('What was it about?')
            print("1. About the dangers of drugs and alcohol. \n 2. SEX ED\n3. math (BORING!!!!11!)")
            if12 = input(insert)
            if if12 == "1":
                print("Alright, you can go play some Ybox or whatever it is that you youngsters do.")
                print("~" * 33)
                print("~" * 6 + "Congrats YOU WON!!!1!" + "~" * 6)
                print("~" * 33)
                os.system('pause')
                exit()
            if if12 == "2":
                print("WHAT THE FACT?!")
                print(died)
                os.system('pause')
                exit()
            if if12 == "3":
                print("MATH?!? BORING?!?? You're a disappointment son!")
                print(died)
                os.system('pause')
                exit()
        elif if1 == "3":
            print("How about you go kiss some math worksheets!")
            print(died)
            os.system('pause')
            exit()
    elif answer1 == '2':
        print("\nWhy so?")
        print("1. A girl I like rejected me..")
        print("2. A bunch of jerks bullied me at lunch")
        print("3. Had some math class.. You know how it is..")
        if21 = input(insert)
        if if21 == '1':
            print("You have girls in your school?!? I thought it's an orthodox school *visible confusion* ")
            print(
                "~" * 100 + "\n Well, you didn't die but dad moved you to the orthodox school, What's the point of living without the cutie from Mr. Johnson's class..\n" + "~" * 100)
            print(died)
            os.system('pause')
            exit()
        if if21 == '2':
            print("\nWhy's that?")
            print("1. I won the kahoot\n2. I have no idea :/ ")
            if211 = input(insert)
            if if211 == '1':
                print("You're a big nerd son! ")
                print(died)
                os.system('pause')
                exit()
            elif if211 == '2':
                print("I told you, you should've taken Krav Maga lessons instead of chess! LOSER!")
                print(died)
                os.system('pause')
                exit()
        if if21 == '3':
            print("\n What's the problem with math??")
            print("1. It's BORING!!!")
            print("2. Nothing, It's great, my favorite subject!")
            if212 = input(insert)
            if if212 == '1':
                print("WHAT?")
                print(died)
                os.system('pause')
                exit()
            if if212 == '2':
                print("Alright, you can go play some Ybox or whatever it is that you youngsters do.")
                print("~" * 33)
                print("~" * 6 + "Congrats YOU WON!!!1!" + "~" * 6)
                print("~" * 33)
                os.system('pause')
                exit()
    elif answer1 == '3':
        print('\nWhat do you mean "boring" how can school be "boring" FGS?!?')
        print("1. A girl rejected me..")
        print("2. I had four hours of MR. Johnson's class. JEEZ it was BORING!!!!")
        print("3. Idk, just played on my phone and skipped class, nothing too interesting")
        if3 = input(insert)
        if if3 == "1":
            age3 = input("YOU ARE TALKING TO GIRLS AT THE AGE OF 10(?) 16(?), WAIT How even old are you young man? ")
            print(
                "ok, let me understand. You're talking to girls at the age of " + age3 + "????????? you're a disgrace son! you're NOT MY SON ANYMORE!")
            print(died)
            os.system('pause')
            exit()
        if if3 == "2":
            print("\nWhat class is \"MR. Johnson's\"??")
            print("1. Math")
            print("2. Sex ED")
            print(
                "3. Let me tell you something dad, I. HAVE. NO. IDEA. I am only looking at the girls' all the cuties are in MR. Johnson's class NGL LOL LMFO GG CLAPPED (or whatever youngsters say nowadays")
            if31 = input(insert)
            if if31 == "1":
                print("MATH?!? Boring? How on earth are you going to have a PHD at the age of 20 with that attitude?")
                print(
                    "\n1. When did I say that I wanted to be a professor at the age of 20?!? \n2. That's ok dad I'm starting to learn to code in Roblox I'll be the next bill gates in no time. \n3. Daddy Chill UwU")
                if311 = input(insert)
                if if311 == "1":
                    print(
                        "Well you clearly said that when you were 2, I have it on tape. How about you stop playing that Ybox of yours and go get some illegal loans for collage?")
                    print(died)
                    os.system('pause')
                    exit()
                if if311 == "2":
                    print("What the heck is roblox? It isn't orthodox isn't it? Show me that roblox thingi")
                    print(
                        "\n1. Show dad your roblox (last game you played was Roblox unchristian intercourse simulator) ")
                    print("2. Smash your Ybox and run away")
                    if3111 = input(insert)
                    if if3111 == "1":
                        print(
                            "What The jesus hell christ jeez holy shit is that sin?? I don't think god will forgive you or me on that one *Went to buy milk a day later and never returned*")
                        print(left)
                        os.system('pause')
                        exit()
                    if if3111 == "2":
                        print("\n Dad: Wha de fuk. COME BACK HERE YOU SCUM!")
                        print(died)
                        os.system('pause')
                        exit()
                if if311 == "3":
                    print("\n *SLAPS YOU WITH A BELT*")
                    print(died)
                    os.system('pause')
                    exit()
            if if31 == "2":
                print("\nWHAT? I AM PAYING FOR THIS SHIT?")
            print(
                "~" * 100 + "\n Well, you didn't die but dad moved you to the orthodox school, What's the point of living without the cutie from Mr. Johnson's class..\n" + "~" * 100)
            print(died)
            os.system('pause')
        if if3 == "3":
            print("\nYou're playing on your phone in class? *SLAPS YOU WITH A BELT*")
            print(died)
            os.system('pause')
            exit()
    else:
        print("You need to enter a number from THE LIST!")

if dad == "2":
    harakiri = "~"*29 + "\n~~You Harakiri'ed yourself!~~\n" + "~"*29
    print("\n-------Attention! everything must be read with Japanese accent-------")
    print("\nNagaski son! how school today? -♦-")
    print("1. Very bad MR. Dad I got A in a test")
    print("2. Good MR. Dad I found the girl of my dreams")
    print("3. Very well MR. Dad, Is there something to eat MR. Dad?")
    dad2 = input(insert)
    if dad2 == '1':
        print("\nYou're a shame to the family son! take sword and Harakiri in your room!!")
        print(died)
        os.system('pause')
        exit()
    if dad2 == '2':
        print("WHAT!? NO GIRL UNTIL 40! YOU'RE A SHAME!")
        print(harakiri)
        os.system('pause')
    if dad2 == '3':
        print("Yes, we have roasted lobster, baked horse and smoked crab.")
        print("1. Ew dad, Do you want me to get salmonella?")
        print("2. mhm.. sounds... yummy. (choose me for a salmonella sidestory) - I haven't written that yet so don't")
        dad21 = input(insert)
        if dad21 == '1':
            print("You no respect family! GO to your room and Harakiri!")
            print(harakiri)
            os.system('pause')
            exit()
        if dad21 == '2':
            print("I told you not to..")
if dad == "3":
    overdose = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n~~You died from overdose!~~ \n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    print("Ayo son, how was your day?")
    print("\n1. It was LIT dad!")
    print("2. What school? I went to hang around with my mate Jack")
    dad3 = input(insert)
    if dad3 == '1':
        print("\nfr? What happened? ")
        print("1. I got C+ in a test!")
        print("2. I got 3 girls at once (Polygamy yes)")
        print("3. I skipped the whole day and robbed elderly woman at the yellow store (static&ben-el reference")
        dad31 = input(insert)
        if dad31 == "1":
            print("\nShit's crazy son... I don't really care tho the whole I've already told you that school is a conspiracy")
            print("1. So can I leave school?")
            print("2. That's not true dad, school is very important for adulthood and for learning new skill")
            dad311 = input(insert)
            if dad311 == "1":
                print("Ye sure whatever, but make sure to hang those weed posters I gave you last week.")
                print("~" * 33)
                print("~" * 6 + "Congrats YOU WON!!!1!" + "~" * 6)
                print("~" * 33)
            if dad311 == "2":
                print("You're talking bullshit, join me with the medicine my friend")
                print(overdose)
                os.system('pause')
                exit()
        if dad31 == "2":
            print("Nice son, that's how I met 3 of my wives which I'm not sure which but one of them is your mom :>")
            print("~" * 33)
            print("~" * 6 + "Congrats YOU WON!!!1!" + "~" * 6)
            print("~" * 33)
        if dad31 == "3":
            print("\nDamn, what you got?")
            print("1. Oh nothing, just some candies and a few papers")
            print("2. At least 10k dad")
            print("3. Oh nothing it was in Grand Theft Vehicle V")
            print("4. Shut up narrator and open the Static & Ben-El song on YT")
            dad312 = input(insert)
            if dad312 == '1':
                print("\nWhat did I sent you to the beginner robber's summercamp for?")
                print(died)
                os.system('pasue')
                exit()
            if dad312 == "2":
                print("\nThat's it? you're a shame son!")
                print(died)
                os.system('pause')
                exit()
            if dad312 == "3":
                print("\b*Belt pulled out*")
                print(died)
                os.system('pause')
                exit()
            if dad312 == "4":
                webbrowser.open('https://www.youtube.com/watch?v=t2fakms1QWo')
    if dad3 == '2':
        print("That's what I'm paying taxes for!")
        print("~" * 33)
        print("~" * 6 + "Congrats YOU WON!!!1!" + "~" * 6)
        print("~" * 33)
        os.system('pause')
        exit()
#ignore me I exist for making the thing below me work
#                                                                   ~~~~ CREATED BY OMRI ~~~~
