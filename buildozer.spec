[app]
title = Instagram Test
package.name = instagramtest
package.domain = com.aarkmaurya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1

# Version Lock (Isse RC-37 wala error khatam ho jayega)
android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools_version = 33.0.0
android.ndk = 25b
android.ndk_api = 21

# Requirements
requirements = python3, kivy==2.3.0, kivymd, pillow, requests, pyjnius, urllib3, certifi

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Architecture
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
