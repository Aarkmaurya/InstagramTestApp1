[app]
title = Instagram Test
package.name = instagramtest
package.domain = com.aarkmaurya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1

# Requirements (Version 2.3.0 is most stable for Actions right now)
requirements = python3, kivy==2.3.0, kivymd, pillow, requests, pyjnius, urllib3, certifi

# Android Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android API & NDK (Inhe change mat karna, ye success combination hai)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

# P4A Branch
p4a.branch = master

# Build settings
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
