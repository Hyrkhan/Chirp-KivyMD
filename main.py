from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (350, 600)
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, NoTransition
import sqlite3


class LoginScreen(Screen):
    pass
class SignUpScreen(Screen):
    pass

class PracticeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"

        screen = Builder.load_file('ScreenDesigns.kv')
        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginScreen(name='loginScreen'))
        screen_manager.add_widget(SignUpScreen(name='signUpScreen'))
        
        self.create_table()
        return screen_manager
    
    def show_data(self, username, password):       
        print(f"Username: {username}")
        print(f"Password: {password}")

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

    def register_validation(self, fname, lname, uname, email, password, cpassword):
        signUp_validate = self.signUp_emptyField_validation(fname, lname, uname, email, password, cpassword)
        if signUp_validate == "Proceed":
            if self.database_lookup(uname, email):
                print("Username or Email already taken")
            elif password != cpassword:
                print("Password and Confirm Password is not the same")
            else:
                print("Can be registered")
        else:
            print(signUp_validate)     

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

    def database_lookup(self, uname, email):
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
        if not fname:
            return "Please enter your First Name"
        elif not lname:
            return "Please enter your Last Name"
        elif not uname:
            return "Please enter your Username"
        elif not email:
            return "Please enter your Email"
        elif not password:
            return "Please enter your Password"
        elif not cpassword:
            return "Please enter your Password again to Confirm"
        else:
            return "Proceed"

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
    
PracticeApp().run()