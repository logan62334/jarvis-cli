#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import signal

import click
import uiautomator2 as u2
from jmdevice.kit.adbkit import ADBKit
from playsound import playsound


def start(d: u2.Device):
    d.app_start(package_name='com.yaya.zone', wait=True)
    d.implicitly_wait(10)
    while True:
        try:
            if d(resourceId="com.yaya.zone:id/cb_all").exists and not d(resourceId="com.yaya.zone:id/cb_all").info[
                'checked']:
                print("点击全选")
                d(resourceId="com.yaya.zone:id/cb_all").click()

            if d(textContains="结算(").exists and d(resourceId="com.yaya.zone:id/cb_all").info['checked']:
                print("点击结算")
                d(textContains="结算(").click()

            if d(text="重新加载").exists:
                print("点击重新加载")
                d(text="重新加载").click()

            if d(text="选择送达时间").exists:
                print("选择送达时间")
                d(text="选择送达时间").click()

            if d(textContains="已约满").exists:
                print("返回购物车")
                d(resourceId="com.yaya.zone:id/iv_dialog_select_time_close").click()
                d(resourceId="com.yaya.zone:id/iv_order_back").click()

            if d(text="下单失败").exists:
                print("下单失败")
                if d(text="返回购物车").exists:
                    print("点击返回购物车")
                    d(text="返回购物车").click()
                    d(resourceId="com.yaya.zone:id/cb_all").click()

            if d(text="立即支付").exists:
                print("点击立即支付")
                d(text="立即支付").click_exists(3)

            if d.current_app()['package'] != 'com.yaya.zone':
                print(d.current_app())
                playsound(os.path.join(os.getcwd(), "jarvis", "cli", "src", "res", "success.mp3"))
        except Exception as e:
            print(e)


@click.command(name='run', help='开启抢菜服务')
def run():
    try:
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        sn = ADBKit().sn
        d = u2.connect(sn)
        d.uiautomator.start()
        start(d=d)
    except Exception as e:
        print(e)


def signal_handler(signum, frame):
    os._exit(0)
