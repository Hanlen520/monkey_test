#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from Base.BasePickle import readInfo
from Base.BaseFile import OperateFile
import xlrd

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class Mailer(object):
    def __init__(self, maillist, mailtitle, mailcontent):
        self.mail_list = maillist
        self.mail_title = mailtitle
        self.mail_content = mailcontent

        self.mail_host = "smtp.qq.com"
        self.mail_user = "84028058"
        self.mail_pass = "lgvyjlhlzbrubhab"
        self.mail_postfix = "qq.com"

    @property
    def sendMail(self):

        me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEMultipart()
        msg['Subject'] = 'appium测试报告'
        msg['From'] = me
        msg['To'] = ";".join(self.mail_list)

        puretext = MIMEText(str(self.mail_content),'html','utf-8')
        #puretext = MIMEText(self.mail_content)
        msg.attach(puretext)

        # jpg类型的附件
        #jpgpart = MIMEApplication(open('/home/mypan/1949777163775279642.jpg', 'rb').read())
        #jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
        #msg.attach(jpgpart)

        # 首先是xlsx类型的附件
        xlsxpart = MIMEApplication(open('../performance_report.xlsx', 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename="performance_report.xlsx")
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

    #读取模板
    mail_content = OperateFile.readTemplate(PATH("../result.html"))
    # 读取结果数据
    # 生成每种机型Monkey性能测试表
    result="<tr>"


    workbook = xlrd.open_workbook("D:\monkey_test\performance_report.xlsx")
    for item in workbook.sheet_by_name("性能数据详情")._cell_values[2]:
        result=result+"<td>"+item+"</td>"
    result=result+"</tr>"

    crash=""
    for item in workbook.sheet_by_name("崩溃日志")._cell_values:
        crash=crash+"<br/>"+item


    mail_content = mail_content.replace("$testResult", result)
    mail_content = mail_content.replace("$crashLog", crash)
    mm = Mailer("guobiao.hu@jieshun.cn", "Monkey稳定性测报告", mail_content)
    res = mm.sendMail
    if res:
        print('--------->>邮件发送成功！')
    else:
        print('--------->>邮件发送失败！')


if __name__ == '__main__':

    #读取模板
    mail_content = OperateFile.readTemplate(PATH("../result.html"))
    # 读取结果数据
    # 生成每种机型Monkey性能测试表
    result="<tr>"


    workbook = xlrd.open_workbook("D:\monkey_test\performance_report.xlsx")
    for item in workbook.sheet_by_name("性能数据详情")._cell_values[2]:
        result=result+"<td>"+str(item)+"</td>"
    result=result+"</tr>"

    crash=""
    for item in workbook.sheet_by_name("崩溃日志")._cell_values:
        crash=crash+"<br/>"+item[0]


    mail_content = mail_content.replace("$testResult", result)
    mail_content = mail_content.replace("$crashLog", crash)
    mm = Mailer("guobiao.hu@jieshun.cn", "Monkey稳定性测报告", mail_content)
    res = mm.sendMail
    if res:
        print('--------->>邮件发送成功！')
    else:
        print('--------->>邮件发送失败！')
