[app]
title = Mustafa App
package.name = mustafaapp
package.domain = org.mustafa
source.dir = .
source.include_exts = py,png,jpg,jpeg
version = 1.0
requirements = python3,kivy
android.api = 35
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.archs = arm64-v8a
