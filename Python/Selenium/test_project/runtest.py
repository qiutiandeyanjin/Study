# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

# =================定义发送邮件==================

to_list = ['qiutiandeyanjin@sina.com', '244894536@qq.com']
server_host = 'smtp.163.com'
username = "qiutiandeyanjin@163.com"
password = "89757xutingyu"


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    # 设置邮件内容和邮件主题
    me = "manager" + "<" + username + ">"
    msg = MIMEText(mail_body, "html", "utf-8")
    msg['Subject'] = Header(u"【测试】自动化测试报告", u"utf-8")
    msg['From'] = me
    msg['To'] = ';'.join(to_list)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(server_host)
        smtp.login(username, password)
        smtp.sendmail(me, to_list, msg.as_string())
        smtp.quit()
        print(u'email has send out !')
    except Exception as e:
        print str(e)


# =========查找测试报告目录，找到最新生成的测试报告文件=========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    # 指定测试用例为当前文件夹下的test_case目录
    test_dir = './test_case'
    test_report = './report'

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test_*.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'测试报告',
                            description=u'用例执行情况')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)  # 发送测试报告
