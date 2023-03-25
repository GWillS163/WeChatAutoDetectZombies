# -*- coding:utf-8 -*-
# Github: GWillS163
# User: 駿清清 
# Date: 3/23/2023 
# Time: 10:23 PM
from wxauto import *


# 获取当前微信客户端
wx = WeChat()
# print(wx.GetLastMessage())  # 获取 最后一条消息


# 获取会话列表
wx.GetSessionList()