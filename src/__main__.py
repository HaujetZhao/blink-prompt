#coding=utf-8

# 程序名：眨眼提示
# 
# 人在正常视物的时候，每分钟眨眼约20次。
# 但认真在看屏幕时，最少的时候一分钟只眨眼2次到3次。
# 眨眼的次数变少会使眼睛暴露在空气中的时间变长，让眼睛干涩，易患上干眼症。
# 
# 程序目的：每过「间隔时长」，就让屏幕瞬间黑一下，提醒用户眨一下眼
# 
# 程序原理：在屏幕上叠加一个黑色全屏贴图，将它的透明度设为 0
#          每过「间隔时长」，就将透明度设为「显现透明度」
#          再经过「显现时长」，就将透明度设回 0
#          其中，「显现透明度」可以控制黑屏的深浅：
#              当它为 1 时，就是全黑；
#              当它为 0.1 时，就是稍微暗一下

import sys
from time import sleep
from PySide2 import QtWidgets
from PySide2.QtCore import Qt, QThread

显现透明度 = 0.2
显现时长 = 0.017
间隔时长 = 5

def main():
    app=QtWidgets.QApplication(sys.argv)

    控件 = QtWidgets.QWidget()
    控件.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    控件.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)
    控件.setStyleSheet('''QWidget{background-color:rgb(0, 0, 0);}''')
    控件.setWindowOpacity(0)
    控件.showFullScreen()
    
    B = BlinkThread(控件,显现透明度, 显现时长, 间隔时长)
    B.start()
    sys.exit(app.exec_())

class BlinkThread(QThread):

    def __init__(self, 
        控件: QtWidgets.QWidget, 
        显现透明度: float, 
        显现时长: float, 
        间隔时长: float, 
        parent=None):

        super(BlinkThread, self).__init__(parent)
        self.控件 = 控件
        self.显现透明度 = 显现透明度
        self.显现时长 = 显现时长
        self.间隔时长 = 间隔时长

    def run(self):
        i = 0
        while True:
            self.控件.setWindowOpacity(self.显现透明度)
            i += 1
            print(f'现身第 {i} 次')
            sleep(self.显现时长)
            self.控件.setWindowOpacity(0)
            sleep(self.间隔时长)

if __name__ == '__main__':
    main()