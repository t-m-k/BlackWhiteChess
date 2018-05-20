#!usr/bin/python3
#-*-coding:utf-8-*-
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt
import sys




class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #self.setGeometry(300, 300, 350, 100)

        #UI-size
        self.resize(QDesktopWidget().availableGeometry().width() / 2,
                    QDesktopWidget().availableGeometry().height() / 4 * 3)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.left(),qr.top() - qr.top()*0.3)
        self.setWindowTitle('ChessBoard')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        #chess background color
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(220, 150, 40, 160))
        chess_background_color_top = self.width() / 2 - self.width() / 10 * 4
        chess_background_color_left = self.height() / 2 - self.height() / 9 * 4
        chess_background_color_width = self.width() / 5 * 4
        chess_background_color_height = self.height() / 5 * 4
        qp.drawRect(chess_background_color_top, chess_background_color_left,
                    chess_background_color_width, chess_background_color_height)

        #chess line
        top_dis = chess_background_color_height/16
        left_dis = chess_background_color_width/16
        grid_width = (chess_background_color_width - 2*left_dis)/4
        grid_height = (chess_background_color_height - 2 * top_dis) / 4
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        qp.setPen(pen)
        for i in range(0,5):
            qp.drawLine(chess_background_color_top + left_dis, chess_background_color_left + top_dis +i*grid_height,
                        chess_background_color_top - left_dis + chess_background_color_width, chess_background_color_left + top_dis+i*grid_height)
            qp.drawLine(chess_background_color_top + left_dis + i*grid_width, chess_background_color_left + top_dis,
                        chess_background_color_top + left_dis + i*grid_width, chess_background_color_left - top_dis + chess_background_color_height)
        #/
        qp.drawLine(chess_background_color_top + left_dis, chess_background_color_left + top_dis + 2 * grid_height,
                    chess_background_color_top + left_dis +  2 * grid_width,chess_background_color_left + top_dis)
        qp.drawLine(chess_background_color_top + left_dis, chess_background_color_left + top_dis + 4 * grid_height,
                    chess_background_color_top + left_dis + 4 * grid_width, chess_background_color_left + top_dis)
        qp.drawLine(chess_background_color_top + left_dis +2* grid_width, chess_background_color_left + top_dis + 4 * grid_height,
                    chess_background_color_top + left_dis + 4 * grid_width, chess_background_color_left + top_dis + 2* grid_height)
        #\
        qp.drawLine(chess_background_color_top + left_dis +  2 * grid_width,chess_background_color_left + top_dis,
                    chess_background_color_top + left_dis + 4 * grid_width,chess_background_color_left + top_dis + 2 * grid_height)
        qp.drawLine(chess_background_color_top + left_dis, chess_background_color_left + top_dis,
                    chess_background_color_top + left_dis + 4 * grid_width, chess_background_color_left + top_dis+ 4 * grid_height)
        qp.drawLine(chess_background_color_top + left_dis, chess_background_color_left + top_dis + 2 * grid_height,
                    chess_background_color_top + left_dis + 2 * grid_width,chess_background_color_left + top_dis + 4 * grid_height)

        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())