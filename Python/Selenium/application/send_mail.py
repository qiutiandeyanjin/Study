# coding=utf-8
import smtplib
from email.mime.text import MIMEText

to_list = ['qiutiandeyanjin@sina.com', '244894536@qq.com']
server_host = 'smtp.163.com'

username = 'qiutiandeyanjin@163.com'
password = '89757xutingyu'


def send(to_list, sub, content):
    """
    :param to_list: 收件人邮箱
    :param sub: 邮件标题
    :param content: 内容
    """
    me = "manager" + "<" + username + ">"
    # _subtype 可以设为html,默认是plain
    msg = MIMEText(content, _subtype='html')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ';'.join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(server_host)
        server.login(username, password)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        print('邮件发送成功')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    send(to_list, u"【测试】使用python发送的邮件", u"<h1>Hello, It's test email.</h1>")
