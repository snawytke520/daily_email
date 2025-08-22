import yagmail
from datetime import datetime
import os

# 从 GitHub Secrets 获取邮箱信息
sender_email = os.environ.get("SENDER_EMAIL")
app_password = os.environ.get("APP_PASSWORD")
receiver_email = os.environ.get("RECEIVER_EMAIL")

# 邮件主题和内容
subject = f"每日报告 - {datetime.now().strftime('%Y-%m-%d')}"
body = "小吴，你好，这是今天的自动报告~"
attachments = []  # 如果有附件，把路径加到这里

try:
    yag = yagmail.SMTP(sender_email, app_password)
    yag.send(to=receiver_email, subject=subject, contents=body, attachments=attachments)
    print("邮件发送成功！")
except Exception as e:
    print("邮件发送失败：", e)
