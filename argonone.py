#!/usr/bin/python3
import smbus
import os
import time
from threading import Thread
import functools

def temp_check():
    try:
        tempFilePath = "/sys/class/thermal/thermal_zone0/temp"
        with open(tempFilePath, "r") as f:
            temp = float(int(f.readline())/1000)

    except IOError:
        temp = 0
    return temp

def set_fan_speed(block):
    adress=0x1a
    bus = smbus.SMBus(1)

    try:
        bus.write_byte(adress, block if block < 100 else 100)
    except IOError:
        print("error")

    return()

def listToTaple(ls):
    return (int(ls[0]), int(ls[1]))

def max_alt(ls):
    return (0,0) if len(ls) == 0 else max(ls)

def fan_speed(config, temp):
    return max_alt(list(filter(lambda x:x[0] < temp, config)))[1]

config = [(65,80), (60,50), (50,10), (0,0)]

def fan_control():
    speed = fan_speed(config, temp_check())
    set_fan_speed(speed)
    return ()

def loop():
    fan_control()
    time.sleep(10)
    return loop()

try:
   t1 = Thread(target = loop)
   t1.start()
except:
   t1.stop()
