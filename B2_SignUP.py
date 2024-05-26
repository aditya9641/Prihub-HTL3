from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image

class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=[50, 150, 50, 50], spacing=20)

        # Image at the top
        image_label = Image(source='Images/Cybernetic_Citadel.png', size_hint=(None, None), size=(200, 200), pos_hint={'center_x': 0.5})
        layout.add_widget(image_label)

        # Username input field
        username_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        username_label = Label(text='Username:', size_hint_x=None, width=100)
        self.username_input = TextInput(hint_text='Enter username')
        username_layout.add_widget(username_label)
        username_layout.add_widget(self.username_input)

        # Email input field
        email_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        email_label = Label(text='Email:', size_hint_x=None, width=100)
        self.email_input = TextInput(hint_text='Enter email')
        email_layout.add_widget(email_label)
        email_layout.add_widget(self.email_input)

        # Password input field
        password_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        password_label = Label(text='Password:', size_hint_x=None, width=100)
        self.password_input = TextInput(hint_text='Enter password', password=True)
        password_layout.add_widget(password_label)
        password_layout.add_widget(self.password_input)

        # Confirm password input field
        confirm_password_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        confirm_password_label = Label(text='Confirm Password:', size_hint_x=None, width=100)
        self.confirm_password_input = TextInput(hint_text='Confirm password', password=True)
        confirm_password_layout.add_widget(confirm_password_label)
        confirm_password_layout.add_widget(self.confirm_password_input)

        layout.add_widget(username_layout)
        layout.add_widget(email_layout)
        layout.add_widget(password_layout)
        layout.add_widget(confirm_password_layout)

        # Sign Up button
        self.signup_button = Button(text='Sign Up', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        self.signup_button.bind(on_press=self.signup)
        layout.add_widget(self.signup_button)

        # Back button
        self.back_button = Button(text='Back', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        self.back_button.bind(on_press=self.go_back)
        layout.add_widget(self.back_button)

        # Error label
        self.error_label = Label(text='', color=(1, 0, 0, 1), size_hint=(None, None), height=20, pos_hint={'center_x': 0.5})
        layout.add_widget(self.error_label)

        self.add_widget(layout)

    def signup(self, instance):
        username = self.username_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_password_input.text

        # Simple validation
        if password != confirm_password:
            self.error_label.text = 'Passwords do not match'
            self.error_label.color = (1, 0, 0, 1) 
        elif not username or not email or not password:
            self.error_label.text = 'Please fill in all fields'
            self.error_label.color = (1, 0, 0, 1) 
        else:
            self.error_label.text = 'Sign Up successful'
            self.error_label.color = (0, 1, 0, 1) 
            # Here you can add code to handle the sign-up logic, like saving the user data

    def go_back(self, instance):
        self.manager.current = 'login'
