[app]
# ऐप का नाम और पैकेज
title = Instagram Test
package.name = instagramtest
package.domain = com.instagramtest
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1

# --- सबसे ज़रूरी हिस्सा (इसे ध्यान से देखें) ---
# इसमें आपकी main.py की सभी लाइब्रेरीज़ शामिल हैं
requirements = python3, kivy==2.1.0, kivymd==1.1.1, requests, openssl, urllib3, certifi, charset-normalizer, idna

# इंटरनेट और स्टोरेज की परमिशन
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

orientation = portrait
fullscreen = 0

# Android सेटिंग्स (ताकि लाइसेंस एरर न आए)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# आर्किटेक्चर (ताकि आपके फोन पर चले)
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
