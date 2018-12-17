import smtplib
import os
import telebot
from skpy import Skype
from email.mime.text import MIMEText



def SentToSkype(message):
        sk = Skype("nectain@ukr.net", "2bhmBNHjU+s,yj" )
#        sk = Skype(tokenFile="/home/gitlab-runner/.tokens-fred.2")
        ch = sk.chats["19:42bd94aef87c496c88067ae137c4b998@thread.skype"]
        ch.sendMsg(message)
def SendToMail(massage,targets):


        smtp_host = 'gw.intecracy.com'
        smtp_port = 587
        username = 'nectain_noreply'
        password = 'r2bhmBNHjU+s,yj1'
        sender = 'nectain_noreply@softengi.com'


        msg = MIMEText(massage)
        msg['Subject'] = 'NECTAIN CI agent'
        msg['From'] = sender
        msg['To'] = targets

        server = smtplib.SMTP(smtp_host, smtp_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()


#SentToSkype()
def SendToTelegram(message):

        TOKEN = "638688644:AAHL4FlM0InqWhi6WQCG4V1PVsiPO_w2fag"
        tb = telebot.TeleBot(TOKEN)
        tb.send_message(-305397413, message)