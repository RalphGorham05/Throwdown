import kivy
kivy.require('1.8.0') # replace with your current kivy version !

#imports for Screens
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout

from random import randint


class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)


class MainScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

class StartScreen(Screen):
    pass

    def pick_numbers(default, number1, number2):
        player_numbers = []

        if not (1 <= number1 <= 100):
            print 'invalid number, one more chance to pick number'
            number1 = input('Enter a number between 1-100 Player 1: ')

        player_numbers.append(number1)
        
        
        if not (1 <= number2 <= 100):
            print 'invalid number, one more chance to pick number'
            number2 = input('Enter a number between 1-100 Player 2: ')

        player_numbers.append(number2)

        return player_numbers


    def home():
        numbers = pick_numbers()

        home = randint(1,100)


        if (abs(numbers[0] - home) < abs(numbers[1] - home)):
            print 'p1 is home'

        elif(abs(numbers[0] - home) == abs(numbers[1] - home)):
            print 'What are the odds!'
            pick_numbers()
    
        else:
            print 'p2 is home'



class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("throwdown.kv")

class ThrowDownApp(App):
    def build(self):
        return presentation

ThrowDownApp().run()

