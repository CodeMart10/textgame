from random import randint
from textwrap import dedent
from sys import exit
class Scene(object):
    def __init__(self):
        pass

class House(Scene):

    def play(self):
        print(dedent("""
        Hello, welcome to my game.
        In this game you will start here in my house.
        Your goal is to deafeat me the narrator, or escape the house.
        Now, I will let you choose where you want to start.

        Type b for 'basement' or a for 'attic'

        """))
        action = input('> ')
        print('GOODLUCK!')
        if action == 'b':
            return 'basement'
        else:
            return 'attic'

        #get user input oto variable


class Basement(Scene):

    def play(self):
        print(dedent("""
        Room
        """))
        action = input('> ')
        if action == 'p':
            return 'dark'
        else:
            return 'haunted'

class Attic(Scene):

    def play(self):
        print(dedent("""
        Dark
        """))
        action = input('> ')
        if action == 'p':
            return 'dark'
        else:
            return 'haunted'

class Haunted(Scene):

    def play(self):
        print(dedent("""
        Haunted
        """))
        action = input('> ')
        if action == 'p':
            return 'done'
        else:
            return 'knockout'

class Done(Scene):
    def play(self):
        print('done')
        return 'done'

class Knockout(Scene):
    def play(self):
        print('you got knocked out')
        exit(1)
