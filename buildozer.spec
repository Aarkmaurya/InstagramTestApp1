[app]
title = Instagram Test
package.name = instagramtest
package.domain = com.aarkmaurya

# (Required) Use these specific versions for stability
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy==2.3.0,requests,urllib3

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# (CRITICAL) API and NDK Settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# (Permissions) 
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (Fix for Java patches)
p4a.branch = master
