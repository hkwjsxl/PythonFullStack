import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# ### 1.邮件内容配置 ###
msg = MIMEText("约吗", 'html', 'utf-8')
msg['From'] = formataddr(["你好", "hankewei0224@126.com"])
msg['Subject'] = "180一晚"

# ### 2.发送邮件 ###
server = smtplib.SMTP_SSL("smtp.126.com")
server.login("hankewei0224@126.com", "EYWWRRRBRCVJAKGR")
server.sendmail("hankewei0224@126.com", "562172420@qq.com", msg.as_string())
server.quit()

