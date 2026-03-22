[app]

# (str) Title of your application
title = Insta Test

# (str) Package name
package.name = instatest_v3

# (str) Package domain (usually com.yourname.project)
package.domain = com.aarkmaurya.v3

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (Method 1)
# Isse 0.3 kar dena taki purani app update ho jaye
version = 0.3

# (str) Application icon
# Yaad rahe aapne GitHub par 'icon.png' upload kar di ho
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) Application requirements
# Isme SQLite, OpenSSL, aur Pillow (Icon ke liye) add kar diya hai
requirements = python3, kivy==2.3.0, kivymd, pillow, requests, pyjnius, openssl, sqlite3, charset-normalizer, idna, urllib3, certifi

# (int) Android API to use
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is to use PythonActivity
android.entrypoint = org.kivy.android.PythonActivity

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (list) Java classes to exclude from indexing
#android.exclude_java_classes =

# (bool) Allow backup
android.allow_backup = True

# (str) python-for-android branch to use
p4a.branch = master

# (int) Log level (2 = verbose)
log_level = 2

# (bool) Display warning if buildozer is run as root (not recommended)
warn_on_root = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (not recommended)
warn_on_root = 1
