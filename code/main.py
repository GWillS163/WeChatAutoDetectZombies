# -*- coding:utf-8 -*-
# Github: GWillS163
# User: 駿清清 
# Date: 3/24/2023 
# Time: 6:40 PM

from libs import *
from appium import webdriver


# 上拉方法
# def swipe_up(distance, time):  # distance为滑动距离，time为滑动时间
#     width = 1080
#     height = 1920  # width 和 height根据不同手机而定
#     driver.swipe(1 / 2 * width, 9 / 10 * height, 1 / 2 * width, (9 / 10 - distance) * height, time)


def getAllFriends(excludeAcc):
    return []


def judgeWhetherBeDeleted(driver, friend):
    def toChatWith(fr):
        clickElement(driver, "搜索按钮")
        driver.find_element_by_id(getElementFullId("搜索框")).send_keys(fr)
        time.sleep(0.5)
        clickElement(driver, "搜索结果", 1)

    def tryTransfer():
        pass

    def recognizePrompt():
        pass

    toChatWith(friend)
    tryTransfer()
    return recognizePrompt()

def judgeWhetherFriend(friendLst):

    allFriendStatus = {}
    for friend in friends:
        pr("正在判断" + friend, end='')
        status = judgeWhetherBeDeleted(friend)
        allFriendStatus[friend] = status
        pr("判断完毕")
    pr("全部判断完毕")
    return allFriendStatus


if __name__ == "__main__":
    pr("正在连接手机")
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    pr("正在进入微信")

    pr("正在获取好友列表")
    friends = getAllFriends(excludeAccounts)
    pr("好友列表获取完毕")
    pr("准备逐一判断")
    allFriendStatus = judgeWhetherFriend(friends)
    print(allFriendStatus)


