[app]

# (str) Title of your application
title = Instagram Test

# (str) Package name
package.name = instagramtest

# (str) Package domain (needed for android packaging)
package.domain = com.instagramtest

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# हमने इसे छोटा और सटीक रखा है ताकि कोई 'Invalid Choice' एरर न आए
requirements = python3, kivy==2.1.0, kivymd==1.1.1, requests, certifi, openssl

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Architecture to build for
android.archs = armeabi-v7a, arm64-v8a

# (bool) enables AndroidX support. Required by KivyMD
android.enable_androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
