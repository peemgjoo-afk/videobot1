[app]
title = VideoBot
package.name = videobot
package.domain = com.videobot.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.1
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license_agreements = True
p4a.bootstrap = sdl2
p4a.fork = kivy
p4a.branch = v2024.01.21
[buildozer]
log_level = 2
