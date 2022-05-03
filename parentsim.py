import os
insert = "Insert your answer [IN NUMBERS!] : "
died = "\n~~~~~~~~~~~~~ \n~~YOU DIED!~~ \n~~~~~~~~~~~~~\n"

print("00000000000000000000000000000000000000000000000")
print("0000000000000000 Dad Simulator 0000000000000000")
print("00000000000000000000000000000000000000000000000")

print('')
print("Good'ay son!")
print("")
print('How was school today?')
print('1. Excellent, had a very informative day!')
print('2. It was ok, not something special.')
print('3. meh.. it was pretty boring...')
print("4. I'm cool show me other options")
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
                print("~"*33)
                print("~"*6+"Congrats YOU WON!!!1!"+"~"*6)
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
        print("~"*100 + "\n Well, you didn't die but dad moved you to the orthodox school, What's the point of living without the cutie from Mr. Johnson's class..\n"+ "~"*100)
        print(died)
        os.system('pause')
        exit()
    if if21 == '2':
        print("\nWhy's that?")
        print("1. I won the kahoot\n2. I have no idea :/ ")
        if211 = input (insert)
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
    print('shutup')

#ignore me I exist for making the thing below me work
os.system('pause')
