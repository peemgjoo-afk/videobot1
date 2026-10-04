[app]
title = VideoBot
package.name = videobot
package.domain = com.videobot.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 2.0
requirements = python3,kivy==2.2.0
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2
[buildozer]
log_level = 2
warn_on_root = 1
