from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder 

topNavBar = """
MDTopAppBar:
    title: "Home"
    left_action_items: [["language-python", lambda x: app.changescreen_to_loginscreen(self)]]
    right_action_items: [["menu"]]
    pos_hint: {'top': 1}
    specific_text_color: app.theme_cls.primary_color
    specific_text_hue: app.theme_cls.primary_hue
    md_bg_color: 0,0,0,1
"""
middleLabel = """
MDLabel:
    text: "This is the Homepage where all the posts of you and your friends show up"
    halign: "center"
"""
botNavBar = """
MDTopAppBar:
    left_action_items: [["earth"], ["chat-processing"], ["account-multiple-outline"], ["account-circle"]]
    specific_text_color: app.theme_cls.primary_color
    specific_text_hue: app.theme_cls.primary_hue
    md_bg_color: 0,0,0,1
"""
createButton = """
MDIconButton:
    icon: "pencil"
    md_bg_color: app.theme_cls.primary_color
    theme_icon_color: "Custom"
    theme_text_color: "ContrastParentBackground"
    icon_color: 0,0,0,1
    pos_hint: {'center_x':0.8, 'center_y':0.1}
    size_hint: (.2, .13)
"""

class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        app = MDApp.get_running_app()
        app.theme_cls.primary_palette = "Green"
        app.theme_cls.primary_hue = "A700"

        self.topBar = Builder.load_string(topNavBar)
        self.middleLabel = Builder.load_string(middleLabel)
        self.bottomBar = Builder.load_string(botNavBar)
        self.create = Builder.load_string(createButton)

        self.add_widget(self.topBar)
        self.add_widget(self.middleLabel)
        self.add_widget(self.bottomBar)
        self.add_widget(self.create)
    

