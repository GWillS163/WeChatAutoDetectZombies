# 介绍 Intro
这是一个基于 Appium 的自动化操作微信的脚本，通过电脑连接安卓手机，实现自动化操作微信检测僵尸粉。 

## 目前自动化微信的方案 (2023年3月25日)
### 手机端控制手机微信
Xposed插件，需要root，但是功能比较强大，可以实现自动转账，自动加好友等。
JS脚本，模拟点击。
无障碍服务，模拟点击。

### 电脑端控制电脑微信
电脑功能比较少（比如不能转账），但原理和开发门槛都比较简单。
- https://github.com/cluic/wxautoapi
- https://github.com/cluic/wxauto
商业工具 WeTools, 功能比较强大，简洁易用，提供免费的个人版。

### 电脑端调试手机微信
Appium，需要安装Appium，安卓SDK，Java JDK，Python等。
直接通过ADB调试工具进行模拟点击，但是可能无法识别按钮和文字。


# 停止开发原因 Stop Development
本来是自用的微信自动化检测。后续发现已经有更完善的项目了，完美解决需要。

下载：[李跳跳·真实好友](https://wwb.lanzouj.com/ihMNw04poswj)



# 项目对你的帮助 Help
- 对于配置部分进行了代码分离，微信更新时自行更改即可。
- 可供参考进行二次开发
- 你可以通过这个项目学习到如何使用 Appium 操作安卓手机
- 你可以通过这个项目学习到如何使用 Python 操作 Appium


# 依赖 Dependencies 
| 名称                | 类型      | 介绍                                      |  
|-------------------|---------|-----------------------------------------|
| Python 3.6.8      | exe软件   |                                         |      
| Appium-Python-Client | Python库 | 安装时会自动安装selenium                        |    
| Selenium          | Python库 | 自动安装Selenium时可能失败，需要自己pip update之后 自行安装 |             
| Appium            | exe软件   | 安卓调试软件                                  |                           
| Android SDK       | 本地文件    | 安卓开发工具包, Appium运行需要                     |                                
| Java JDK          | 本地文件    | Java开发工具包, Appium运行需要                   |     
文件获取：https://pan.baidu.com/s/1jd60QGI68VZB-pRhBCcAwQ  
提取码：6f49
                   |         |                                         |

# 参考 Reference
- 主要参考： [Python+Appium实现删除微信“僵尸好友”](https://blog.csdn.net/qq_40208154/article/details/111145904)
- [用 Python + Appium 的方式自动化清理微信僵尸好友](https://blog.csdn.net/lau_jw/article/details/114592571)
- Appium 如何定位元素 [Appium定位元素的几种方法总结](https://blog.csdn.net/lovedingd/article/details/111058898)
- 新版本Appium-python-client的弃用方法说明 [find_element_by_id方法被弃用,有删除线](https://blog.csdn.net/weixin_65588529/article/details/122575724)
- [安装Appium-Python-Client时 Selenium 无法安装](https://blog.csdn.net/xiaochen0913/article/details/112530397)
- [官方文档Appium-Python-Client 1.2.0](https://appium.io/docs/en/about-appium/intro/#getting-started)