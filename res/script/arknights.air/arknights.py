# -*- encoding=utf8 -*-
__author__ = "euqorab"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from random import randint
import ctypes, sys, os
from win32api import ShellExecute


ADB_PATH = "Z:\\AirtestIDE_2019-04-16_py3_win64\\AirtestIDE_2019-04-16_py3_win64\\airtest\\core\\android\\static\\adb\\windows\\adb"
PACKAGE_NAME = "com.hypergraph.arknights.air.bilibili"


dynamic = True

def setup():
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
                "Android://127.0.0.1:5037/127.0.0.1:7555?ori_method=ADBORI&&touch_method=ADBTOUCH",
        ])


def runCmd(cmd):
    print(cmd)
    os.popen(cmd)
    

def connect():
    sleep(5)
    cmd = "%s connect 127.0.0.1:7555" % ADB_PATH
    runCmd(cmd)

    cmd = "%s shell am force-stop com.hypergryph.arknights.bilibili" % ADB_PATH
    runCmd(cmd)
    sleep(1)
    cmd = "%s shell am start com.hypergryph.arknights.bilibili/com.u8.sdk.SplashActivity" % ADB_PATH
    runCmd(cmd)
    sleep(15)
    touch(Template(r"tpl1610290399337.png", record_pos=(-0.176, -0.242), resolution=(1440, 810)))


    
def changeAccount():
    global dynamic
    while dynamic:
        sleep(10)
        a = exists(Template(r"tpl1610288215507.png", record_pos=(0.463, -0.238), resolution=(1440, 810)))

        if a:
            touch(list(a))
            sleep(5)
            touch(list(a))
            sleep(3)
            touch(list(a))
            sleep(3)
            break
        elif exists(Template(r"tpl1610286821315.png", record_pos=(0.257, -0.155), resolution=(1440, 810))):
            touch(Template(r"tpl1610286632204.png", record_pos=(-0.461, -0.249), resolution=(1440, 810)))
            sleep(1)
            touch(Template(r"tpl1610286645946.png", record_pos=(0.173, -0.105), resolution=(1440, 810)))
            sleep(1)
            touch(Template(r"tpl1610286654249.png", record_pos=(0.157, 0.115), resolution=(1440, 810)))
            sleep(5)
            touch(Template(r"tpl1610286676984.png", record_pos=(0.122, -0.092), resolution=(1440, 810)))
            sleep(1)
            touch(Template(r"tpl1610286687319.png", record_pos=(-0.081, 0.085), resolution=(1440, 810)))
            sleep(1)
            touch(Template(r"tpl1610286710878.png", record_pos=(0.08, 0.081), resolution=(1440, 810)))
            break
    print("change account done")


def run():
    global dynamic
    while dynamic:
        sleep(10)
        if exists(Template(r"tpl1610286821315.png", record_pos=(0.257, -0.155), resolution=(1440, 810))):
            touch(Template(r"tpl1610286821315.png", record_pos=(0.257, -0.155), resolution=(1440, 810)))

            sleep(2)
            touch(Template(r"tpl1610286917143.png", record_pos=(-0.314, 0.234), resolution=(1440, 810)))
            sleep(1)
            touch(Template(r"tpl1610286928794.png", record_pos=(-0.36, -0.025), resolution=(1440, 810)))
            sleep(1)
            touch(Template(r"tpl1610286948826.png", record_pos=(0.244, -0.144), resolution=(1440, 810)))
            sleep(1)

        while dynamic:
            flag = False
            while dynamic:
                print("loop: epoch start")
                a = exists(Template(r"tpl1583919420230.png", record_pos=(0.419, 0.231), resolution=(1440, 810)))
                if not a:
                    a = exists(Template(r"tpl1597251391927.png", record_pos=(0.417, 0.232), resolution=(1440, 810)))

                if a:
                    if exists(Template(r"tpl1610286974980.png", record_pos=(0.395, 0.181), resolution=(1440, 810))):
                        touch(Template(r"tpl1610286985440.png", record_pos=(0.395, 0.183), resolution=(1440, 810)))

                    a = list(a)
                    a[0] += randint(0, 20) - 10
                    a[1] += randint(0, 20) - 10
                    touch(a)
                    sleep(randint(200, 500) / 100)
                    break
    #             elif exists(Template(r"tpl1596385036488.png", record_pos=(-0.001, 0.112), resolution=(1440, 810))):
    #                 return
    
                sleep(1)

            while dynamic:
                print("loop: team")
                a = exists(Template(r"tpl1566967469871.png", record_pos=(0.304, 0.092), resolution=(2280, 1080)))
                if a:
                    a = list(a)
                    a[0] += randint(0, 20) - 10
                    a[1] += randint(0, 20) - 10
                    touch(a)
                    sleep(80)
                    break
                elif exists(Template(r"tpl1577687907919.png", record_pos=(0.198, 0.115), resolution=(1440, 810))):
                    a = exists(Template(r"tpl1577685734118.png", record_pos=(0.349, 0.169), resolution=(1440, 810)))
                    touch(a)
                    flag = True
                    break
                elif exists(Template(r"tpl1593587437591.png", record_pos=(0.128, -0.024), resolution=(1440, 810))):
                    touch(Template(r"tpl1593585791584.png", record_pos=(0.108, 0.169), resolution=(1440, 810)))
    #                 sleep(1080)
    #                 flag = True
                    dynamic = False
                    print("break")
                    break
    #                 sleep(2)
    #                 touch(Template(r"tpl1593586065769.png", record_pos=(-0.29, -0.249), resolution=(1440, 810)))
    #                 sleep(2)
    #                 touch(Template(r"tpl1593586101193.png", record_pos=(0.349, -0.251), resolution=(1440, 810)))
    #                 return
    #             elif exists(Template(r"tpl1596385036488.png", record_pos=(-0.001, 0.112), resolution=(1440, 810))):
    #                 return
                sleep(1)

            if flag:
                continue

            while dynamic:
                print("loop: epoch done")
                if exists(Template(r"tpl1566967661834.png", record_pos=(-0.315, 0.174), resolution=(2280, 1080))):
                    sleep(randint(200, 500) / 100)
                    touch([150+randint(0, 300) - 150, 150+randint(0, 300) - 150])
                    print("epoch done")
                    break
                sleep(1)
                    



def Task():

    for count in range(50):
        if exists(Template(r"tpl1593586306105.png", record_pos=(0.336, -0.17), resolution=(1440, 810))):
            touch(Template(r"tpl1593586306105.png", record_pos=(0.336, -0.17), resolution=(1440, 810)))
        elif exists(Template(r"tpl1594108915798.png", record_pos=(0.002, -0.208), resolution=(1440, 810))):
            touch([1000, 1000])

        else:
            return

        sleep(2)

        



def openSimulator():
    mumu_path = "C:\\Program Files (x86)\\MuMu\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe"
    ShellExecute(0, "open", mumu_path, "", "", 1)
    sleep(15)
    
def closeSimulator():
    cmd = "%s shell am force-stop com.hypergryph.arknights.bilibili" % ADB_PATH
    runCmd(cmd)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# print("ark script run start...")
# openSimulator()
# auto_setup()
# connect()
# changeAccount()
# run()
# closeSimulator()
# print("ark script run end")
    
if __name__ == "__main__":
    print("ark script run start...")
    openSimulator()
    setup()
    connect()
    changeAccount()
    run()
    closeSimulator()
    print("ark script run end")

