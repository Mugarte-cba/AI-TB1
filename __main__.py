import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

class Home(GridLayout):
    def __init__(self):
        super(Home,self).__init__()
        self.Presentation=Presentation()
        self.Login=Login()

        self.add_widget(self.Presentation)
        self.add_widget(self.Login)

class Presentation(BoxLayout):
    def __init__(self):
        super(Presentation,self).__init__()

class Login(GridLayout):
    def __init__(self):
        super(Login,self).__init__()

class Select_Car(GridLayout):
    def __init__(self):
        super(Select_Car,self).__init__()


class HillclimApp(App):
    title = 'Algoritmo Hill Climbing'
    def build(self):
        return Home()

if __name__=='__main__':
    HillclimApp().run()