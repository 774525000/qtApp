# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PySide2.QtWebEngineWidgets import *


class WebView(QWebEngineView):
    def createWindow(self, window_type):
        print(window_type)
        return self


class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        view = WebView()

        view.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        view.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        view.settings().setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
        view.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        view.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        view.setUrl(QUrl('https://www.baidu.com'))

        layout = QVBoxLayout()
        layout.addWidget(view)
        self.setLayout(layout)
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())
