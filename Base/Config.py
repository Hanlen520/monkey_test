# /usr/bin/env python
# -*- encoding: utf-8 -*-
import random
import configparser
class Config:

    conf = configparser.ConfigParser()
    conf.read("config//config.ini","utf-8")
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

    email_address = conf.get("monkey","email_address").split(",")
    email_subject = conf.get("monkey", "email_subject")
    email_content = conf.get("monkey", "email_content")
    attach_name = conf.get("monkey", "attach_name")

    mail_host = conf.get("monkey","mail_host")
    mail_user = conf.get("monkey","mail_user")
    mail_pass = conf.get("monkey","mail_pass")
    mail_postfix = conf.get("monkey","mail_postfix")

if __name__ == '__main__':
    print(Config.mail_postfix)
