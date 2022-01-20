# from requests_html import HTMLSession
#
# with HTMLSession() as session:
#     r = session.get('https://jisho.org/search/%E6%84%9B%20%23kanji')
#
# content = r.html
#
#
# def findJishoContent(content, name, **kwargs):
#     if kwargs.get('xpath'):
#         try:
#             return content.xpath(f'{name}')[0].text
#         except Exception as ex:
#             print(f'Warning: {ex.__class__.__name__}, in traslateProcess in findJishoContent [1].')
#             return None
#     else:
#         try:
#             return content.find(f'.{name}', first=True).text
#         except Exception as ex:
#             print(f'Warning: {ex.__class__.__name__}, in traslateProcess in findJishoContent [2].')
#             return None
#
#
# print([findJishoContent(content, 'kanji-details__main-meanings'), findJishoContent(content, 'grade'),
#        findJishoContent(content, '//*[@id="result_area"]/div/div[1]/div[1]/div/div[2]/div[1]', xpath=True),
#        findJishoContent(content, '//*[@id="result_area"]/div/div[1]/div[1]/div/div[2]/div[2]/dl', xpath=True),
#        findJishoContent(content, '//*[@id="result_area"]/div/div[1]/div[1]/div/div[2]/div[3]/dl', xpath=True)])
#
#
# a = input()
#
#
# print(a)
#
# import random
# a = list(range(100))
#
# print(a)
# random.shuffle(a)
# print(a)
#
#
# a = ['1','2']
#
# b = ''.join([str(av) for av in a])
# print(b)
#
#
# def testYield():
#     a = 0
#     for i in range(1000):
#         print("a")
#         yield i
#         a += i
#
#
# test = testYield()
# print(test)
#
#
# import requests
# from bs4 import BeautifulSoup
#
# a = requests.get('https://jisho.org/search/%E9%BB%99%20%23kanji')
# print(a.content)
#
#
# for i in range(10):
#     print(i)

# while True:
#     print('a')




class MainWindow(QtGui.):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(277, 244)
        self.statusbar = QtGui.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirm Exit...",
                                            "Are you sure you want to exit ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            event.accept()


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
