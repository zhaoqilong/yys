#coding:utf-8
import sys
import itchat
from itchat.content import *


def lc():
    print("微信登录成功")
def ec():
    print("微信已经退出")

on_first_in_group = '阴阳师辅助脚本开启！！'

class WechatUtils(object):

    def __init__(self, user):
        itchat.auto_login(loginCallback=lc, exitCallback=ec)
        a = itchat.search_friends(user)
        self.user = a[0]['UserName']
        itchat.send_msg(on_first_in_group, toUserName=self.user)
        itchat.run(debug=True, blockThread=False)

    def send_question(self, res):
        itchat.send_msg(res, toUserName=self.user)

    def logout(self):
        itchat.logout()