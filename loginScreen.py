from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivy.lang import Builder 

headerlabel = """
MDLabel:
    text: "Log in to Chirp"
    halign: "center"
    pos_hint: {'center_x':0.5, 'center_y':0.6}
    font_style: "H4"
"""
username_helper = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_left: "account"
    pos_hint: {'center_x':0.5, 'center_y':0.5}
    size_hint_x: None 
    width: 220
    md_bg_color: app.theme_cls.primary_dark
"""
password_helper = """
MDTextField:
    hint_text: "Enter password"
    helper_text: "or click on forgot password"
    helper_text_mode: "on_focus"
    icon_left: "lock"
    pos_hint: {'center_x':0.5, 'center_y':0.4}
    size_hint_x: None 
    width: 220
    md_bg_color: app.theme_cls.primary_dark
"""
loginbuttonhelper = """
MDRoundFlatButton:
    md_bg_color: 0,0,0,1
    line_color: 0,0,0,1
    text_color: "white"
    text: "Log in" 
    font_size: 20
    size_hint_x: 0.6
    size_hint_y: 0.08
    pos_hint: {'center_x':0.5, 'center_y':0.25}
    on_release: app.show_data(self)
"""
signuptext = """
MDLabel:
    text: "Don't have an account?"
    theme_text_color: "Hint"
    halign: "center"
    pos_hint: {'center_x':0.44, 'center_y':0.18}
    font_style: "Caption"
"""
Signuplink = """
MDTextButton:
    text: "Sign up"
    underline: True
    halign: "center"
    font_style: "Caption"
    pos_hint: {"center_x": 0.69, "center_y": 0.18}
    theme_text_color: "Custom"
    text_color: 0.3607, 0.3882, 1
    on_release: app.changescreen_to_signupscreen(self)
"""
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        app = MDApp.get_running_app()
        app.theme_cls.primary_palette = "Green"
        app.theme_cls.primary_hue = "A700"

        self.label = Builder.load_string(headerlabel)
        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)
        self.signuptext = Builder.load_string(signuptext)
        self.terms = Builder.load_string(Signuplink)
        self.button = Builder.load_string(loginbuttonhelper) 

        self.ids.username = self.username
        self.ids.password = self.password

        self.add_widget(self.label)
        self.add_widget(self.username)
        self.add_widget(self.password)
        self.add_widget(self.signuptext)
        self.add_widget(self.terms)
        self.add_widget(self.button)