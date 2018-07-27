# /usr/bin/env python
# -*- encoding: utf-8 -*-
import random
import configparser
class Config:

    conf = configparser.ConfigParser()
    conf.read("../config//config.ini","utf-8")
    # apk包名
    package_name = conf.get("monkey","package_name")
    # 默认设备列表
    device_dict = {}
    # 网络
    net = conf.get("monkey","net")
    # monkey seed值，随机产生
    monkey_seed = str(random.randrange(1, 1000))
    # monkey 参数
    monkey_parameters = conf.get("monkey","monkey_parameters")
    # log保存地址
    log_location = conf.get("monkey","log_location")
    #性能数据存储目录
    info_path = conf.get("monkey","info_path")


