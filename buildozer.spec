[app]
title = VideoBot PRO
package.name = videobotpro
package.domain = com.videobot.pro
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 3.0
requirements = python3,kivy==2.3.1
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license_agreement = True
android.permissions = CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
p4a.branch = master

[buildozer]
log_level = 2

[app:android]
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license_agreement = True
android.permissions = CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
p4a.branch = master
