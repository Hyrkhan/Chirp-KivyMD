from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager 
from kivy.core.window import Window
Window.size = (350, 600)
from loginScreen import LoginScreen
from signupScreen import SignUpScreen
from homeScreen import HomeScreen

class ChirpApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()

        loginScreen = LoginScreen(name='loginScreen')
        screen_manager.add_widget(loginScreen)
        signUpScreen = SignUpScreen(name='signUpScreen')
        screen_manager.add_widget(signUpScreen)
        homeScreen = HomeScreen(name='homeScreen')
        screen_manager.add_widget(homeScreen)

        return screen_manager
    
    def show_data(self, obj):
        loginScreen = self.root.get_screen('loginScreen')
        username_widget = loginScreen.ids.username
        password_widget = loginScreen.ids.password

        username = username_widget.text
        password = password_widget.text

        if username == "":
            check_string = "Please enter username"
        else:
            check_string = username

        if password == "":
            check_pass = "Please enter password"
        else:
            check_pass = password

        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        home_button = MDFlatButton(text="Home", on_release=self.home_action)

        self.dialog = MDDialog(
            title="Details",
            text=f"{check_string}\n{check_pass}",
            buttons= [home_button,close_button]
        )

        self.dialog.open()

    def home_action(self, obj):
        screen_manager = self.root
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'homeScreen'
        self.dialog.dismiss()
        
    def close_dialog(self, obj):
        self.dialog.dismiss()

    def changescreen_to_signupscreen(self, obj):
        screen_manager = self.root
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'signUpScreen'
    def changescreen_to_loginscreen(self, obj):
        screen_manager = self.root
        screen_manager.transition.direction = 'right'
        screen_manager.current = 'loginScreen'
   

if __name__ == "__main__":
    ChirpApp().run()
