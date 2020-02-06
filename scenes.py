from random import randint
from textwrap import dedent
from sys import exit


class Scene(object):
    def __init__(self):
        pass

#House scene
class House(Scene):

    def play(self):
        #starting scene
        print(dedent("""
        Hello, welcome to my game.
        In this game you will start here in my house.
        Your goal is to deafeat the enemy I put in the house,
        or escape the house.

        Now, I will let you choose where you want to start.

        Type b for 'basement'
        or a for 'attic'

        GOODLUCK!
        """))
        action = input('=> ')

        #choice for start
        if action == 'b':
            return 'basement'
        else:
            return 'attic'

#Basement scene
class Basement(Scene):

    def play(self):
        #basement dialogue
        print(dedent("""
        You chose the basement
        The enemy is in the kitchen on the second floor.
        Good news is he cant hear you walking around, but
        bad news is you only have one escape route.

        Type c to look around the basement
        Type e to run up the stairs to the basement door
        """))
        action = input('=> ')

        #basement choice 'look around'
        if action == 'c':
            print(dedent("""
            You quick scan around,
            the basement has a ping pong table,
            a living room with a TV and toys,
            and an office setup with a computer.

            If you want to use one of those as weapon
            Type
            ping pong paddle
            ken barbie doll
            the office computer

            if you dont want anything say type nothing
            """))
            action = input('=> ')

            if item != '':
                print(dedent(f"ok so you picked up {action} not sure how that will help"))
                print(dedent('now that you have your awesome weapon you run upstairs.'))
                return 'kitchen'
            else:
                print('you think you break the rules?')
                return "knockout"

        #basement choice 'run upstairs'
        else:
            print(dedent("""
            You run upstairs and push the door open quietly,
            or assert dominance and slam it open?
            q for quietly
            capital D for DOMINANT!"""))

            action = input('=> ')

            #Basement path e choice "look quietly"
            if action == 'q':
                print("""
                you open the door quietly and peek in to see the
                monster standing in the kitchen""")
                return 'kitchen'

            #Basement path e choice "BE DOMINANT"
            if action == 'D':
                print(dedent("""
                You launch the door open and the monster looks at you
                immediately and runs at you.
                Now you wish you had a weapon huh?
                """))
                return 'knockout'

#Attic scene
class Attic(Scene):

    #Attic dialogue
    def play(self):
        print(dedent("""
        Attic
        why would you choose attic lol
        the monster hears your footsteps and sprint up the upstairs
        """))
        return 'knockout'

#Kitchen Scene
class Kitchen(Scene):

    #Kitchen dialogue
    def play(self):
        print(dedent("""
        now is the time to throw you weapon at him if you have one
        the monster doesn't see you,

        type fight or flight
        """))

        action = input('=> ')

        #Kitchen choice "fight"
        if action == 'fight':
            return 'knockout'

        #Kitchen choice "flight"
        else:
            print(dedent("""
            you look to see 2 ways out
            press f for front door
            press r for living room
            """))

            action = input('=> ')

            #Kitchen path flight choice "front door"
            if action == 'f':
                print(dedent('well done you life'))
                return 'done'

            #Kitchen path flight choice "living room"
            else:
                print(dedent("""
                lmao why the hell would you not pick the big front
                door to freedom,
                dumbass...
                """))
                return 'knockout'

#Won game
class Done(Scene):
    def play(self):
        print(dedent("""
        you made it out but your not that cool
        cuz this game was easy
        """))
        exit(1)

#Game over
class Knockout(Scene):
    def play(self):
        print('you got knocked out')
        exit(1)
