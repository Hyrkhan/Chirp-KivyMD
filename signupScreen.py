from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivy.lang import Builder 

headerlabel = """
MDLabel:
    text: "Sign Up to Chirp"
    halign: "center"
    pos_hint: {'center_x':0.5, 'center_y':0.77}
    font_style: "H4"
"""
firstname_helper = """
MDTextField:
    hint_text: "Enter firstname"
    icon_left: "account-details"
    pos_hint: {'center_x':0.5, 'center_y':0.68}
    size_hint_x: None 
    width: 220
"""
lastname_helper = """
MDTextField:
    hint_text: "Enter lastname"
    icon_left: "account-details"
    pos_hint: {'center_x':0.5, 'center_y':0.60}
    size_hint_x: None 
    width: 220
"""
username_helper = """
MDTextField:
    hint_text: "Enter username"
    icon_left: "account-edit"
    pos_hint: {'center_x':0.5, 'center_y':0.52}
    size_hint_x: None 
    width: 220
"""
email_helper = """
MDTextField:
    hint_text: "Enter email"
    icon_left: "email-edit"
    pos_hint: {'center_x':0.5, 'center_y':0.44}
    size_hint_x: None 
    width: 220
"""
password_helper = """
MDTextField:
    hint_text: "Enter password"
    icon_left: "lock-open-plus"
    pos_hint: {'center_x':0.5, 'center_y':0.36}
    size_hint_x: None 
    width: 220
"""
confirmpassword_helper = """
MDTextField:
    hint_text: "Confirm password"
    icon_left: "lock-check"
    pos_hint: {'center_x':0.5, 'center_y':0.28}
    size_hint_x: None 
    width: 220
"""
signupbuttonhelper = """
MDRoundFlatButton:
    md_bg_color: 0,0,0,1
    text_color: "white"
    text: "Sign Up" 
    font_size: 20
    size_hint_x: 0.6
    size_hint_y: 0.08
    pos_hint: {'center_x':0.5, 'center_y':0.17}
    border: False
    line_color: 0,0,0,1
"""
logintext = """
MDLabel:
    text: "Already have an account?"
    theme_text_color: "Hint"
    halign: "center"
    pos_hint: {'center_x':0.43, 'center_y':0.1}
    font_style: "Caption"
"""
Loginlink = """
MDTextButton:
    text: "Log in"
    underline: True
    halign: "center"
    font_style: "Caption"
    pos_hint: {"center_x": 0.69, "center_y": 0.1}
    theme_text_color: "Custom"
    text_color: 0.3607, 0.3882, 1
    on_release: app.changescreen_to_loginscreen(self)
"""
class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)

        app = MDApp.get_running_app()
        app.theme_cls.primary_palette = "Green"
        app.theme_cls.primary_hue = "A700"

        self.label = Builder.load_string(headerlabel)
        self.firstname = Builder.load_string(firstname_helper)
        self.lastname = Builder.load_string(lastname_helper)
        self.username = Builder.load_string(username_helper)
        self.email = Builder.load_string(email_helper)
        self.password = Builder.load_string(password_helper)
        self.confirmpassword = Builder.load_string(confirmpassword_helper)
        self.logintext = Builder.load_string(logintext)
        self.Loginlink = Builder.load_string(Loginlink)
        self.signupButton = Builder.load_string(signupbuttonhelper)

        self.add_widget(self.label)
        self.add_widget(self.firstname)
        self.add_widget(self.lastname)
        self.add_widget(self.username)
        self.add_widget(self.email)
        self.add_widget(self.password)
        self.add_widget(self.confirmpassword)
        self.add_widget(self.logintext)
        self.add_widget(self.Loginlink)
        self.add_widget(self.signupButton)