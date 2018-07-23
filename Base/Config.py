# /usr/bin/env python
# -*- encoding: utf-8 -*-
import random

class Config:
    # apk包名
    package_name = "com.jieshun.jslife"
    # 默认设备列表
    device_dict = {}
    # 网络
    net = "wifi"
    # monkey seed值，随机产生
    monkey_seed = str(random.randrange(1, 1000))
    # monkey 参数
    monkey_parameters = "--throttle 300 --ignore-crashes --ignore-timeouts --pct-touch 60 --pct-trackball 12 --pct-appswitch 5 --pct-syskeys 10 --pct-motion 13 -v -v 2000"
    # log保存地址
    log_location = "D:\\monkey_test\\log\\"
    #性能数据存储目录
    info_path = "D:\\monkey_test\\info\\"
