# -*- coding:utf-8 -*-
# Github: GWillS163
# User: 駿清清 
# Date: 3/24/2023 
# Time: 6:40 PM

# define button id

# 本次开发时与他人开发时的id不同，所以需要一个映射表
idMap = {
    '发消息': 'khu',
    '通讯录': 'kht',
    '界面列表': 'hga',
    "搜索按钮": 'gss',  # j63
    "搜索框": 'cd6',
    "搜索结果": 'j6c',

    "通讯录是否到底": 'bml',

    # 转账界面
    "聊天加号": "b3q",
    "转账": "ve",
    "转账数字": "ffn",  # 1
    "转账确认": "ffw",
    "转账弹窗": "od",
    "转账弹窗文字": "guv",  # 请你确认你和他（她）的朋友关系是否正常 / 你不是对方的朋有


}

desired_caps = {
    "platformName": "Android",  # 系统
    "platformVersion": "11.0.0",  # 系统版本号  注意修改为自己的版本号
    "deviceName": "meng_mi",  # 设备名
    # "appPackage": "com.tencent.tim",  # 包名
    "appPackage": "com.tencent.mm",  # 包名
    "appActivity": ".ui.LauncherUI",  # app 启动时主 Activity
    'unicodeKeyboard': True,  # 使用自带输入法
    'noReset': True  # 保留 session 信息，可以避免重新登录
}

width = 1080
height = 1920  # width 和 height根据不同手机而定
myWeChatName = '駿清清'

excludeAccounts = [myWeChatName, '文件传输助手', '新的朋友', '群聊', '标签', '公众号', '微信团队']


def getElementFullId(cname):
    apkName = 'com.tencent.mm'
    idSuffix = ':id/'
    return apkName + idSuffix + idMap[cname]

