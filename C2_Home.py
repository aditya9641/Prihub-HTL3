from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label

class HomeScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        # Sidebar
        self.sidebar = BoxLayout(orientation='vertical', size_hint=(None, 1), width=200)
        self.sidebar_label = Label(text='Sidebar', size_hint_y=None, height=50)
        self.sidebar.add_widget(self.sidebar_label)

        # Content
        self.content = BoxLayout(orientation='vertical', pos=(200, 0))

        # Top bar button to open sidebar
        self.sidebar_button = Button(text='Open Sidebar', size_hint=(None, None), size=(100, 50))
        self.sidebar_button.bind(on_release=self.toggle_sidebar)

        # Circular button to open dropdown menu
        self.dropdown_button = Button(text='Menu', size_hint=(None, None), size=(50, 50), pos_hint={'right': 1})
        self.dropdown = DropDown()
        for index in range(5):
            btn = Button(text='Option {}'.format(index), size_hint_y=None, height=30)
            self.dropdown.add_widget(btn)
        self.dropdown_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.dropdown_button, 'text', x))

        # Add widgets to content layout
        self.content.add_widget(self.sidebar_button)
        self.content.add_widget(self.dropdown_button)

        # Add widgets to main layout
        self.add_widget(self.sidebar)
        self.add_widget(self.content)

    def toggle_sidebar(self, instance):
        if self.sidebar.x == 0:
            self.sidebar.x -= self.sidebar.width
        else:
            self.sidebar.x = 0


