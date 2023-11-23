#!/usr/bin/env python3
import argparse
from argparse import RawTextHelpFormatter
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time, datetime
import signal
import sys
#import argparse
is24hourFormat = True
is3digitFormat = False

hat = SenseHat()

welcome = True
isAM = False
hours_color = (0, 255, 0)
minutes_color = (0, 0, 255)
seconds_color = (255, 0, 0)
is24hour_color = (255, 255, 0)
isAM_color = (255, 0, 0)
off_color = (0, 0, 0)


def takeArguments():
    global is24hourFormat
    global is3digitFormat 
    # Create command line parameter parser object.
    parser = argparse.ArgumentParser(description="How to use: \nUse -f to set the hour format\nUse -d to set the digit format"
                                     + "\n\nFor Joystick\n\nPress UP to set the clock to 24 hour format\nPress DOWN to set the clock to 12 hour format"
                                     + "\nPress LEFT to set the digit format to 3\nPress RIGHT to set the digit format to 6", formatter_class=RawTextHelpFormatter)
    # Add optional command line parameters.
    parser.add_argument('-f', action='store', dest='hour_format', default='24', help='12 hour or 24 hour format. Default is 24')
    parser.add_argument('-d', action='store', dest='digit_format', default='6', help='3-digit format or 6-digit format. Default is 6')
    # Perform actual command line parameter parsing.
    args = parser.parse_args()
    if args.hour_format == "12":
        is24hourFormat = False
    if args.digit_format == "3":
        is3digitFormat = True


def signalHandler(signalNumber, frame):
            '''Shows a message before ending the program'''
            hat.show_message("Programmet slutter", 0.02)
            sys.exit(1)

#funktionen som sørger for at vise tiden
def DisplayBinaryTime(value, row, color, is24hour):
    '''Takes the hour/minute/second, row, color and if it's 24 hour format and then sets the pixels accordingly'''
    #formaterer value til binær
    binær_str = "{0:8b}".format(value)
    #looper gennem en range fra 0 til 8 for at finde ud af om min diode skal være tændt eller slukket
    if not is24hour:
        hat.set_pixel(0, 7, is24hour_color)
        if isAM:
            hat.set_pixel(2, 7, isAM_color)
        else:
            hat.set_pixel(2, 7, off_color)
    else:
        hat.set_pixel(0, 7, off_color)
        hat.set_pixel(2, 7, off_color)

    for x in range(0, 8):
        if binær_str[x] == '1':
            #diode tændt
            hat.set_pixel(x, row, color)
        else:
            #diode slukket
            hat.set_pixel(x, row, off_color)


def Show24hourFormat(extended):
    '''Takes a boolean to set up the clock in a 24 hour format in a 3-digit format or 6-digit format'''
    t = datetime.datetime.now()
    Show24hourFormat = True
    if extended:
        timestampStr = t.strftime("%H%M%S")
        timeList = [int(x) for x in timestampStr]
        i = 0
        for num in timeList:
            if i < 2:
                color = hours_color
            elif i > 1 and i < 4:
                color = minutes_color
            elif i > 3 and i < 6:
                color = seconds_color

            DisplayBinaryTime(num, i, color, Show24hourFormat)
            i += 1
    else:
        DisplayBinaryTime(t.hour, 0, hours_color, Show24hourFormat)
        DisplayBinaryTime(t.minute, 1, minutes_color, Show24hourFormat)
        DisplayBinaryTime(t.second, 2, seconds_color, Show24hourFormat)

    time.sleep(0.0001)

def Show12hourFormat(extended):
    '''Takes a boolean to set up the clock in a 12 hour format in a 3-digit format or 6-digit format'''
    t = datetime.datetime.now()
    Show24hourFormat = False
    global isAM

    if t.hour > 12:
        isAM = False
    else:
        isAM = True

    if extended:
        timestampStr = t.strftime("%I%M%S")
        timeList = [int(x) for x in timestampStr]
        i = 0
        for num in timeList:
            if i < 2:
                color = hours_color
            elif i > 1 and i < 4:
                color = minutes_color
            elif i > 3 and i < 6:
                color = seconds_color

            DisplayBinaryTime(num, i, color, Show24hourFormat)
            i += 1
    else:
        DisplayBinaryTime(ConvertTime(str(t.hour)), 0, hours_color, Show24hourFormat)
        DisplayBinaryTime(t.minute, 1, minutes_color, Show24hourFormat)
        DisplayBinaryTime(t.second, 2, seconds_color, Show24hourFormat)
        time.sleep(0.0001)

def ConvertTime(input):
    '''Takes an hour input and returns the hour as an int in 12 hour format.'''
    hours = input[0:2]
    hours = int(hours)

    if hours > 12:
        hours -= 12

    return hours

signal.signal(signal.SIGINT, signalHandler)
signal.signal(signal.SIGTERM, signalHandler)
#signal.signal(signal.SIGKILL, signalHandler)

takeArguments()

while True:
    for event in hat.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                is24hourFormat = True
                hat.clear()
            if event.direction == "down":
                is24hourFormat = False
                hat.clear()
            if event.direction == "right":
                is3digitFormat = False
                print("hehe1")
                hat.clear()
            if event.direction == "left":
                is3digitFormat = True
                print("hehe2")
                hat.clear()
            if event.direction == "middle":
                signalHandler(100,255)
        if event.action == "held":
            temp = hat.get_temperature()
            print(temp)



    
        
    
    if welcome:
        hat.show_message("Programmet starter", 0.02)
        welcome = False
    
    if is24hourFormat and is3digitFormat:
        Show24hourFormat(extended=False)
    
    if is24hourFormat and not is3digitFormat:
        Show24hourFormat(extended=True)
    
    if not is24hourFormat and is3digitFormat:
        Show12hourFormat(extended=False)

    if not is24hourFormat and not is3digitFormat:
        Show12hourFormat(extended=True)