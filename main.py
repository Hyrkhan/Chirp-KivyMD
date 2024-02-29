from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (350, 600)
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, NoTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
import sqlite3
import re

class LoginScreen(Screen):
    pass
class SignUpScreen(Screen):
    pass
class HomeScreen(Screen):
    pass
class MessageScreen(Screen):
    pass
class FriendScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass
class AddFriendScreen(Screen):
    pass

class PracticeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"

        menu_list = [
            {
                "viewclass": "OneLineListItem",
                "text": "Switch to Dark Mode",
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Settings",
                "on_release": lambda x = "Settings": self.settings_action()
            }
        ]
        self.menu = MDDropdownMenu(
            items = menu_list,
            width_mult = 4
        )

        screen = Builder.load_file('ScreenDesigns.kv')
        screen_manager = ScreenManager()
        
        screen_manager.add_widget(LoginScreen(name='loginScreen'))
        screen_manager.add_widget(SignUpScreen(name='signUpScreen'))
        screen_manager.add_widget(HomeScreen(name='homeScreen'))
        screen_manager.add_widget(MessageScreen(name='messageScreen'))
        screen_manager.add_widget(FriendScreen(name='friendScreen'))
        screen_manager.add_widget(ProfileScreen(name='profileScreen'))
        screen_manager.add_widget(SettingsScreen(name="settingsScreen"))
        screen_manager.add_widget(AddFriendScreen(name="addFriendScreen"))
        
        self.create_table()
        return screen_manager

    def dropdown(self, button):
        self.menu.caller = button
        self.menu.open()
        
    def create_table(self):
        conn = sqlite3.connect('practice_db.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users(
                  id INTEGER PRIMARY KEY,
                  fname TEXT,
                  lname TEXT, 
                  uname TEXT,
                  email TEXT,
                  password TEXT
                  )""")
        
        conn.commit()
        conn.close()

    def popup_error(self, string):
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)

        self.dialog = MDDialog(
            title="Error!",
            text = string,
            buttons= [close_button]
        )
        self.dialog.open()

    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()

    def login_validation(self, username, password):   
        error_string = ""    
        if not username:
            error_string = "Please enter Username to Login"
        elif not password:
            error_string = "Please enter Password to Login"
        else:
            result = self.username_password_validation(username, password)
            if result != "Proceed":
                error_string = result 
            else:
                self.home_action() 
        if error_string:
            self.popup_error(error_string)

    def username_password_validation(self, uname, password):
        conn = sqlite3.connect('practice_db.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE uname = ?", (uname,))
        result1 = c.fetchone()

        if result1 is None:
            conn.close()
            return "User has not been registered yet"
        else:
            c.execute("SELECT password FROM users WHERE uname = ?", (uname,))
            passw = c.fetchone()
            conn.close()
            if passw[0] != password:
                return f"Password is Incorrect"
            else:
                return "Proceed"

    def register_validation(self, fname, lname, uname, email, password, cpassword):
        error_string = ""
        signUp_validate = self.signUp_emptyField_validation(fname, lname, uname, email, password, cpassword)
        if signUp_validate == "Proceed":
            if self.username_email_validation(uname, email):
                error_string = "Username or Email already taken"
            elif not self.validate_email(email):
                error_string = "Please enter a valid email address"
            elif password != cpassword:
                error_string = "Password and Confirm Password is not the same"
            else:
                print("Can be registered")
        else:
            error_string = signUp_validate       
        if error_string:
            self.popup_error(error_string)  

    def register(self, fname, lname, uname, email, password):
        conn = sqlite3.connect('practice_db.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (fname, lname, uname, email, password) VALUES (:fname, :lname, :uname, :email, :password)",
                  {
                      'fname': fname,
                      'lname': lname,
                      'uname': uname,
                      'email': email,
                      'password': password,
                  })
        print("Register successfull")
        conn.commit()
        conn.close()

    def username_email_validation(self, uname, email):
        conn = sqlite3.connect('practice_db.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE uname = ?", (uname,))
        result = c.fetchone()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        result2 = c.fetchone()

        if result is None and result2 is None:
            conn.close()
            return False
        else:
            conn.close()
            return True
        
    def signUp_emptyField_validation(self, fname, lname, uname, email, password, cpassword):
        params = {
            "First Name": fname, "Last Name": lname, "Username": uname, "Email": email, "Password": password, "Password again to Confirm" : cpassword
            }
        for key, val in params.items():
            if not val:
                return f"Please enter your {key}"
        return "Proceed"     

    def validate_email(self, email):
        pattern = r'^\S+@(\w+\.)?(\w+\.(com|edu|gov|co|govt)(\.\w+)?)$'
        if re.match(pattern, email):
            return True
        else:
            return False

    def changescreen_to_signupscreen(self):
        screen_manager = self.root
        screen_manager.transition = SlideTransition()
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'signUpScreen'

    def changescreen_to_loginscreen(self):
        screen_manager = self.root
        screen_manager.transition = SlideTransition()
        screen_manager.transition.direction = 'right'
        screen_manager.current = 'loginScreen'
    
    def home_action(self):
        screen_manager = self.root
        screen_manager.transition = SlideTransition()
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'homeScreen'
        self.close_dialog()

    def back_home_action(self):
        screen_manager = self.root
        screen_manager.transition = NoTransition()
        screen_manager.current = 'homeScreen'

    def message_action(self):
        screen_manager = self.root
        screen_manager.transition = NoTransition()
        screen_manager.current = 'messageScreen'
    
    def back_message_action(self):
        screen_manager = self.root
        screen_manager.transition = NoTransition()
        screen_manager.current = 'messageScreen'
        
    def friends_action(self):
        screen_manager = self.root
        screen_manager.transition = NoTransition()
        screen_manager.current = 'friendScreen'

    def back_friends_action(self):
        screen_manager = self.root
        screen_manager.transition = NoTransition()
        screen_manager.current = 'friendScreen'

    def profile_action(self):
        screen_manager = self.root
        screen_manager.transition = NoTransition()
        screen_manager.current = 'profileScreen'

    def settings_action(self):
        screen_manager = self.root
        self.beforeScreen = screen_manager.current
        screen_manager.transition = SlideTransition()
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'settingsScreen'
        self.menu.dismiss()

    def back_to_beforeScreen(self):
        screen_manager = self.root
        screen_manager.transition = SlideTransition()
        screen_manager.transition.direction = 'right'
        screen_manager.current = self.beforeScreen

    def addFriend_action(self):
        screen_manager = self.root
        self.beforeScreen = screen_manager.current
        screen_manager.transition = SlideTransition()
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'addFriendScreen'

PracticeApp().run()
