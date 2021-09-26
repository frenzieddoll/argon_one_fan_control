#!/usr/bin/python3
import smbus
# import RPi.GPIO as GPIO
import os
import time
from threading import Thread
import functools

def temp_check():
    try:
        tempfp = open("/sys/class/thermal/thermal_zone0/temp", "r")
        temp = tempfp.readline()
        tempfp.close()
        val = float(int(temp)/1000)
    except IOError:
        val = 0
    return val

def set_fan_speed(block):
    adress=0x1a

    # rev = GPIO.RPI_REVISION
    # if rev == 2 or rev == 3:
    #     bus = smbus.SMBus(1)
    # else:
    #     bus = smbus.SMBus(0)
    bus = smbus.SMBus(1)

    try:
        bus.write_byte(adress, block if block < 100 else 100)
        return ()
    except IOError:
        return ()

def listToTaple(ls):
    return (int(ls[0]), int(ls[1]))

def open_config():
    try:
        config_file_path = os.path.expanduser("~") + "/.config/systemd/user/fanctl.config"
        config_file=open(config_file_path)
        config_list = list(map(listToTaple,[s.strip().split() for s in config_file.readlines()]))
        config_file.close()
    except:
        config_list = [(65,80), (60,50), (50,10), (0,0)]
    return config_list

def max_alt(ls):
    return (0,0) if len(ls) == 0 else max(ls)


def fan_speed(config, temp):
    return max_alt(list(filter(lambda x:x[0] < temp, config)))[1]

config = open_config()

def fan_control(config):
    temp = temp_check()
    speed = fan_speed(config, temp)
    set_fan_speed(speed)
    print(config)
    print(temp)
    print(speed)

def loop():
    fan_control(config)
    time.sleep(10)
    return loop()

try:
	t1 = Thread(target = loop)
	t1.start()
except:
	t1.stop()
