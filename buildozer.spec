[app]

# (str) Title of your application
title = Instagram Test

# (str) Package name
package.name = instagramtest

# (str) Package domain (needed for android packaging)
package.domain = com.instagramtest

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# ध्यान दें: इसमें openssl, certifi और platform के लिए ज़रूरी चीजें जोड़ दी गई हैं
requirements = python3, kivy==2.1.0, kivymd==1.1.1, requests, certifi, openssl, urllib3, idna, charset-normalizer

# (str) Custom source folders for requirements
# (list) Garden requirements
# (str) Presplash of the application
# (str) Icon of the application
# (list) Supported orientations
orientation = portrait

# (list) Permissions
# इंटरनेट एक्सेस के लिए यह बहुत ज़रूरी है
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
android.ndk = 25b

# (bool) indicate if the application should be signed for testing
android.debug_artifact = True

# (str) Android entry point, default is ok for Kivy based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy based app
android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Architecture to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a, arm64-v8a

# (bool) enables AndroidX support. Required by KivyMD
android.enable_androidx = True

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# (list) The Android architectures to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# (str) python-for-android branch to use, if not master
#p4a.branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

