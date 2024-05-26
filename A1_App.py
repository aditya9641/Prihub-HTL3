from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown

from B1_Login import LoginScreen
from B2_SignUP import SignUpScreen
# from C2_Home import HomeScreen

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        # self.add_widget(Label(text='Welcome to the Home Page'))
        
        self.add_widget(Image(source='images/Logo.png', size_hint=(0.5, 0.5), pos_hint={'center_x':0.5}))
        self.channels_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        self.channels_layout.bind(minimum_height=self.channels_layout.setter('height'))

        # Example channels (replace with your own channel names)
        channel_names = ['Channel 1', 'Channel 2', 'Channel 3', 'Channel 4', 'Channel 5']

        for channel_name in channel_names:
            channel_button = Button(text=channel_name, size_hint_y=None, height=40)
            self.channels_layout.add_widget(channel_button)

        self.add_widget(self.channels_layout)

class MainApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MainApp().run()


class MyApp(App):
    def build(self):
        # Set window size
        Window.size = (500, 900)
        
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignUpScreen(name='signup'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    MyApp().run()
    
