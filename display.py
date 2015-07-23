import kivy
kivy.require('1.8.0') # replace with your current kivy version !

#imports for Screens
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout


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


class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("throwdown.kv")

class ThrowDownApp(App):
    def build(self):
        return presentation

ThrowDownApp().run()

