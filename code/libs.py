# -*- coding:utf-8 -*-
# Github: GWillS163
# User: 駿清清 
# Date: 3/24/2023 
# Time: 7:08 PM
from config import *
import time


def pr(strings, color="default", end="\n", *args):
    print(strings, end=end, *args)


def clickElement(driver, step, index=0):
    driver.find_elements_by_id(getElementFullId(step))[index].click()
    time.sleep(0.5)
