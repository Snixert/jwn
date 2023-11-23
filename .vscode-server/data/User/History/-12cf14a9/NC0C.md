---
title: Binary Clock
section: 1
header: User Manual
footer: hello_sense 1.0.0
date: November 22, 2023
---

# NAME
hello_sense, Binary Clock program

# OPTIONS
**-h** 
: display help message

**-f** 
: Hour format, choose between 12 or 24, default value is 24.

**-d** 
: Hour format, choose between 12 or 24, default value is 24.

# EXAMPLES
**hello_sense.py -f 12 -d 3**
: Sets the clock to use 12 hour format and 3-digit format.

# Joystick Instructions
**UP**
: Press UP to change the clock to use 24 hour format.

**DOWN**
: Press DOWN to change the clock to use 12 hour format.

**LEFT**
: Press LEFT to change the clock to use 3-digit format.

**RIGHT**
: Press RIGHT to change the clock to use 6-digit format.

**MIDDLE**
: Press MIDDLE to turn off the clock.

# Service
**Enable**
: To enable the service type: sudo systemctl enable test.service

**Reload**
: to reload after enable type: sudo systemctl daemon-reload

**Start**
: To start the service type: sudo systemctl start test.service

**Stop**
: To stop the service type: sudo systemctl stop test.service

**Restart**
: To restart the service type: sudo systemctl restart test.service

**Check**
: To check the service type: sudo systemctl check test.service