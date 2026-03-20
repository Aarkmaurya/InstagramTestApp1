[app]
title = Instagram Test
package.name = instagramtest
package.domain = com.instagramtest
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1

# 1. Requirements में Pillow और Requests जोड़ दिए हैं (Instagram जैसे काम के लिए ज़रूरी हैं)
requirements = python3,kivy==2.1.0,kivymd==1.1.1,pillow,requests,urllib3

# 2. Permissions (Internet ज़रूरी है)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

orientation = portrait
fullscreen = 0

# 3. Android API Levels (यह सबसे ज़रूरी है)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# 4. Architecture (ताकि नए और पुराने दोनों फ़ोन्स में चले)
android.archs = armeabi-v7a, arm64-v8a

# 5. Allow Backup
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
