# 在Windows上安装music21
[原文链接](https://web.mit.edu/music21/doc/installing/installWindows.html)

## 获取Python
Python是一款简单但强大的编程语言。music21即基于Python开发，在本教程中，你将会用Python和music21开发自己的程序。

Windows用户请安装Python3.8或以上版本

要下载Python，请访问[https://www.python.org/downloads/](https://www.python.org/downloads/)，点击"Windows installer"链接。这应该是第一个链接。将文件保存至桌面并双击运行

> 译注：Python也可以从[微软商店](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7)安装。如果没有管理员权限，则应从微软商店安装Python。
 
检查Python已正确安装：Windows搜索IDLE，运行，输入`2+2`。如果显示`4`则python已正确安装，可以安装music21

## 更新Python
如果你已经安装了Python，打开IDLE，输出的第一行会包含版本号。music21支持Python3.7或以上。

如果你的Python版本太旧，下载一个新版的并安装。

## 安装music21
打开命令提示符，输入：
```
pip install music21
```
这将下载并安装music21。如果你已经装了music21想更新，请运行：
```
pip install --upgrade music21
```
检查music21已正确安装：运行IDLE，输入`import music21`。等待几秒钟后应该继续显示提示符`>>>`。（如果显示找不到`music21`，那么你的系统可能装了多个Python，请全部卸载后重新开始）。

接下来配置`music21`，让它找到Musescore或Finale等辅助软件。在IDLE中输入：
```
import music21
music21.configure.run()
```
或者在命令提示符中输入：
```
python3 -m music21.configure
```
## 安装后
安装成功后，你就可以从[用户指南，第2章：音符](../userguide/2.ipynb)开始学习

## 安装帮助
如果你按照本文的方法安装music21却仍然遇到问题，重新从头开始并小心安装。如果仍然遇到问题，联系music21 Google Group，也许某个人能提供帮助：

[https://groups.google.com/g/music21list](https://groups.google.com/g/music21list)