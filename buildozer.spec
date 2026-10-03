[app]
title = VideoBot
package.name = videobot1
package.domain = org.test.videobot1
source.dir =.
version = 0.1
requirements = python3,kivy==2.3.0,pyjnius==1.6.1
orientation = portrait
[buildozer]
log_level = 2
[app:android]
p4a.branch = master
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
