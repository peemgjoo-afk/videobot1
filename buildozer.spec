[app]
title = VideoBot1
package.name = videobot1
package.domain = com.peemgjoo.videobot1
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.allow_backup = True
android.permissions = INTERNET

# ถ้าใน main.py นายมี kivymd ให้เปลี่ยนบรรทัด requirements ข้างบนเป็น
# requirements = python3,kivy,kivymd
