#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import subprocess

def main():
    dev_cmd = "ls /dev/input/ | grep \"js0\""
    fg = 0

    while True:
        result = subprocess.Popen(dev_cmd, stdout=subprocess.PIPE,shell=True).communicate()[0].strip('\n')
        if fg == 0 and result == "js0":
            led_cmd = "echo 1 > /dev/myled0"
            subprocess.call(led_cmd, shell=True)
            fg = 1
        if fg == 1 and result != "js0":
            fg = 0
        print "fg :",fg
        time.sleep(0.5)
        
if __name__ == "__main__":
    main()
