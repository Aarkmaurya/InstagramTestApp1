[app]
title = Instagram Test
package.name = instagramtest
package.domain = com.aarkmaurya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1

# Requirements: openssl aur certifi zaroori hain HTTPS (Telegram) ke liye
requirements = python3, kivy==2.3.0, kivymd, pillow, requests, pyjnius, openssl, certifi, charset-normalizer, idna, urllib3

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.0
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
