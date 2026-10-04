[app]
title = Video Bot
package.name = videobot
package.domain = com.videobot.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2
p4a.branch = master
