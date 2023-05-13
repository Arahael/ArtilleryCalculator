import kivy
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Global variables
pressure = NumericProperty(None)
temperature = NumericProperty(None)
distance = NumericProperty(None)
ownElevation = NumericProperty(None)
targetElevation = NumericProperty(None)
sideWind = NumericProperty(None)
wind = NumericProperty(None)

rFlightTime = NumericProperty(None)
rFinalElevation = NumericProperty(None)
rFinalWindage = NumericProperty(None)

#Classes for different windows
class MainWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('ballcalc.kv')

def calculate(self):
    print("Tak")

class BallCalc(App):
    def build(self):
        return kv

if __name__ == "__main__":
    try:
        BallCalc().run()
    except Exception as e:
        print(f"An error occurred: {e}")