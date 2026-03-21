[app]
title = Instagram Test
package.name = instagramtest
package.domain = com.aarkmaurya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
version = 0.1

requirements = python3,kivy==2.1.0,kivymd==1.1.1,requests,pyjnius

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
