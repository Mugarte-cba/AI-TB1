import kivy
kivy.require('1.0.7')

import csv
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.properties import ObjectProperty

class Home(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.Presentation=Presentation()
        self.Login=Login()

        self.add_widget(self.Presentation)
        self.add_widget(self.Login)

class Presentation(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class Login(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        username=ObjectProperty(None)
        password=ObjectProperty(None)

        def btn():
            myapp.screen_manager.current='Select_Car'

        def user_find(self,file):
            for row in file:
                if row[0] == self.username.text:
                    print("username found", self.username.text)
                    user_found = [row[0], row[1]]
                    pass_check(user_found,self.username.text)

        def pass_check(self,user_found):
            if user_found[1] == self.password.text:
                print("password match")
                self.btn()
            else:
                print("password not match")



        with open("users.txt", "r") as file:
            file_reader = csv.reader(file)
            user_find(file_reader,self.username.text)
            file.close()

class Select_Car(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class HillclimApp(App):
    title = 'Algoritmo Hill Climbing'
    def build(self):
        self.screen_manager=ScreenManager()

        self.home=Home()
        screenHome=Screen(name='Home')
        screenHome.add_widget(self.home)
        self.screen_manager.add_widget(screenHome)

        self.select_Car=Select_Car()
        screenSelect_Car=Screen(name='Select_Car')
        screenSelect_Car.add_widget(self.select_Car)
        self.screen_manager.add_widget(screenSelect_Car)

        return self.screen_manager

if __name__=='__main__':
    myapp=HillclimApp()
    myapp.run()