[app]

# (section) Title of your application
title = Instagram Test

# (section) Package name
package.name = instagramtest

# (section) Package domain (needed for android packaging)
package.domain = com.aarkmaurya

# (section) Source code where the main.py live
source.dir = .

# (section) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (section) Application version
version = 0.1

# (section) Application requirements
# KivyMD aur SSL ke liye ye requirements zaroori hain
requirements = python3, kivy==2.3.0, kivymd, pillow, requests, pyjnius, urllib3, certifi, charset-normalizer, idna

# (section) Garden requirements
garden_requirements =

# (section) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (section) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (section) Supported orientations
orientation = portrait

# (section) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (section) Android API, SDK and NDK directory (Dhyan se dekho, yahi success hai)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.build_tools_version = 33.0.0

# (section) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (section) Allow backup
android.allow_backup = True

# (section) python-for-android branch
p4a.branch = master

# (section) Screen handling
fullscreen = 0

[buildozer]

# (section) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (section) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

# (section) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (section) Path to bin directory
# bin_dir = ./bin
