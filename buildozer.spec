[app]
title = VideoBot
package.name = videobot
package.domain = com.videobot.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 2.0
requirements = python3==3.11.9,kivy==2.3.0
orientation = portrait
[buildozer]
log_level = 2
[app:android]
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 28c
android.archs = arm64-v8a
android.accept_sdk_license_agreement = True
p4a.branch = master
p4a.bootstrap = sdl2
