#!/bin/bash

cd /usr/local/blender-2.79-linux-glibc219-x86_64/ && ./blender -b --python /home/antoine/3DMaps/Main.py
cd /home/antoine
google-chrome test.html
