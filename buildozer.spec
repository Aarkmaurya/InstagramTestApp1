[app]
# ऐप की बेसिक जानकारी
title = Instagram Test
package.name = instagramtest
package.domain = com.instagramtest
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1

# --- सबसे ज़रूरी: Requirements ---
# इसमें kivy, kivymd, requests और SSL के लिए ज़रूरी लाइब्रेरीज़ हैं
requirements = python3, kivy==2.1.0, kivymd==1.1.1, requests, openssl, urllib3, certifi, charset-normalizer, idna

# इंटरनेट और स्टोरेज परमिशन
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
orientation = portrait
fullscreen = 0

# --- Android SDK/NDK सेटिंग्स (स्टेबल वर्जन) ---
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True

# आर्किटेक्चर (ताकि आपके फ़ोन पर ऐप चले)
android.archs = armeabi-v7a, arm64-v8a

# बिल्ड टूल्स (इन्हें खाली छोड़ दें, GitHub Actions खुद मैनेज करेगा)
# android.sdk_path = 
# android.ndk_path = 

[buildozer]
log_level = 2
warn_on_root = 1
