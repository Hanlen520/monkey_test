#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from Base.Config import Config

class Mailer(object):
    def __init__(self, maillist, mailtitle, mailcontent):
        self.mail_list = maillist
        self.mail_title = mailtitle
        self.mail_content = mailcontent

        self.mail_host = Config.mail_host
        self.mail_user = Config.mail_user
        self.mail_pass = Config.mail_pass
        self.mail_postfix = Config.mail_postfix

    def sendMail(self):

        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEMultipart()
        msg['Subject'] = 'Monkey 测试'
        msg['From'] = me
        msg['To'] = ";".join(self.mail_list)

        # puretext = MIMEText('<h1>你好，<br/>'+self.mail_content+'</h1>','html','utf-8')
        puretext = MIMEText(self.mail_content)
        msg.attach(puretext)

        # jpg类型的附件
        #jpgpart = MIMEApplication(open('/home/mypan/1949777163775279642.jpg', 'rb').read())
        #jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
        #msg.attach(jpgpart)

        # 首先是xlsx类型的附件
        xlsxpart = MIMEApplication(open(Config.attach_name, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename=Config.attach_name)
        msg.attach(xlsxpart)

        # mp3类型的附件
        # mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
        # mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
        # msg.attach(mp3part)

        # pdf类型附件
        # part = MIMEApplication(open('foo.pdf', 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
        # msg.attach(part)

        try:
            s = smtplib.SMTP()  # 创建邮件服务器对象
            s.connect(self.mail_host)  # 连接到指定的smtp服务器。参数分别表示smpt主机和端口
            s.login(self.mail_user, self.mail_pass)  # 登录到你邮箱
            s.sendmail(me, self.mail_list, msg.as_string())  # 发送内容
            s.close()
            return True
        except Exception as e:
            print(str(e))
            return False
def sendEmail():
    # send list
    mailto_list = Config.email_address
    mail_title = Config.email_subject
    mail_content = Config.email_content
    mm = Mailer(mailto_list, mail_title, mail_content)
    res = mm.sendMail()
    print('发送完成！')


if __name__ == '__main__':
    # send list
    mailto_list = ["guobiao.hu@jieshun.cn", "zhandong.han@jieshun.cn"]
    mail_title = 'Monkey测试'
    mail_content = '-------->>Monkey测试<<--------'
    mm = Mailer(mailto_list, mail_title, mail_content)
    res = mm.sendMail()
    print(res)
