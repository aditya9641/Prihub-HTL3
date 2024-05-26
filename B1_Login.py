from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from B2_SignUP import SignUpScreen


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Add background image
        background = Image(source='Images/Blocks.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(background)

        layout = BoxLayout(orientation='vertical', padding=[50, 250, 50, 50], spacing=20)
        
        # LOGO at the top
        image_label = Image(source='Images/Cybernetic_Citadel.png', size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(image_label)
        
        # Create a horizontal box layout for each input field
        username_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(350, 40), pos_hint={'center_x': 0.4, 'y': 0.4})
        password_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(350, 40), pos_hint={'center_x': 0.4, 'y': 0.35})
       
        # Username input field
        username_label = Label(text='Username:', size_hint_x=None, width=100)
        self.username_input = TextInput(hint_text='Enter username')
        username_layout.add_widget(username_label)
        username_layout.add_widget(self.username_input)

        # Password input field
        password_label = Label(text='Password:', size_hint_x=None, width=100)
        self.password_input = TextInput(hint_text='Enter password', password=True)
        password_layout.add_widget(password_label)
        password_layout.add_widget(self.password_input)

        self.add_widget(username_layout)
        self.add_widget(password_layout)

        # Login button
        self.login_button = Button(text='Login', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.4, 'y': 0.28})
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)
        self.error_label = Label(text='', color=(1, 0, 0, 1), pos_hint={'center_x': 0.5})
        layout.add_widget(self.error_label)

        self.add_widget(layout)

        # Sign UP
        self.SignUP_button = Button(text='Sign UP', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.6, 'y': 0.28})
        self.SignUP_button.bind(on_press=self.go_to_signup)
        self.add_widget(self.SignUP_button)
        
    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        # Simple validation
        if username == 'a' and password == '123':
            self.error_label.text = 'Login successful'
            self.manager.current = 'main'
        else:
            self.error_label.text = 'Invalid username or password'
            
    def go_to_signup(self, instance):
        self.manager.current = 'signup'



