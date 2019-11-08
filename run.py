#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 17:13
# @Author  : Lqq/linqingqing
# @Site    : 
# @File    : run.py
# @Software: PyCharm

import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import traceback
import requests
import time

from bs4 import BeautifulSoup as bs
from PyQt5 import QtCore, QtWidgets
from view.subdomain import Ui_Form
from util.database import Db
from util.web_subdomain import WebUrl


class Worker(QtCore.QThread):
    sig = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0
        self.domain = None

    def __del__(self):
        self.working = False
        self.wait()

    def setVal(self, val):
        self.domain = str(val)

        ##执行线程的run方法
        self.start()

    def run(self):
        count = 0
        while self.working == True:
            url = WebUrl().get_url(self.domain, count)

            response = requests.get(url, headers=WebUrl().headers)
            response.encoding = 'utf-8'
            data = response.content
            if response.status_code == 200:
                count = count+1
                soup = bs(data, 'html.parser')
                divlist = soup.find_all("div", attrs={"class": "result c-container"})
                self.sig.emit(divlist)
                time.sleep(1)

class Combosel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Combosel, self).__init__(parent)

        self.ui_sel = Ui_Form()
        self.ui_sel.setupUi(self)

        # 清理结果集
        self.ui_sel.result.clear()

        # 创建新线程，将自定义信号sinOut连接到slotAdd()槽函数
        self.thread = Worker()
        self.thread.sig.connect(self.get_data)

        # 连接自己的槽函数
        self.ui_sel.pushButton.clicked.connect(self.onActivatedpushButton)


    # 获取网页数据
    def get_data(self,divlist):
        print(divlist)
        domain = ''
        title = ''
        try:
            d = self.ui_sel.domain.text()
            host = self.ui_sel.host.text()
            port = self.ui_sel.port.text()
            user = self.ui_sel.user.text()
            passwd = self.ui_sel.passwd.text()
            db = self.ui_sel.db.text()
            charset = self.ui_sel.charset.text()
            for div in divlist:
                a = div.find("a", attrs={'class': 'c-showurl', 'style': 'text-decoration:none;'})
                h = div.find("h3", attrs={'class': 't'})
                if a:
                    domain = a.get_text()
                    star = 0
                    end = 0
                    if domain.find("//") != -1:
                        star = domain.find("//") + 2
                    if domain.find(d) != -1:
                        end = domain.find(domain) + len(d)
                    domain = domain[star:end]
                if h:
                    title = h.get_text()

                if Db(host, port, user, passwd, db, charset).get_website(domain) == 0:
                    Db(host, port, user, passwd, db, charset).insert_domain(title, domain)
                    self.ui_sel.result.insertPlainText("标题：" + title + "数据添加成功\n")

        except:
            traceback.print_exc()


    # 点击
    def onActivatedpushButton(self):
        try:
            # 清理结果集
            self.ui_sel.result.clear()
            domain = self.ui_sel.domain.text()
            self.thread.setVal(domain)
            self.thread.start()
        except:
            traceback.print_exc()
            

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        Appcombosel = Combosel()
        Appcombosel.show()
        sys.exit(app.exec_())
    except:
        traceback.print_exc()
