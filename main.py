from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(396, 570)
        Form.setMinimumSize(QtCore.QSize(396, 531))
        Form.setMaximumSize(QtCore.QSize(406, 1000))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(2, 3, 3, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(381, 43))
        self.label.setMaximumSize(QtCore.QSize(381, 43))
        font = QtGui.QFont()
        font.setFamily("Nova Flat")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(229, 229, 229);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 385, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setAlignment(Qt.AlignBottom)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 67))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setMinimumSize(QtCore.QSize(351, 51))
        self.textEdit.setMaximumSize(QtCore.QSize(351, 51))
        self.textEdit.setStyleSheet("background-color: rgb(232, 232, 232);\n"
"border-radius: 6px;\n"
"padding-right: 30px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(41, 51))
        self.pushButton.setMaximumSize(QtCore.QSize(41, 51))
        self.pushButton.setStyleSheet("background-color: rgb(232, 232, 232);\n"
"border-radius: 6px;\n"
"border-bottom-left-radius: 0px;\n"
"border-top-left-radius: 0px;\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignBottom)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "CHAT WITH ME"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:131074;\"><br /></p></body></html>"))
        self.pushButton.setShortcut(_translate("Form", "Return"))



        self.pushButton.clicked.connect(self.add_label)
        self.text_num = 1
        self.messages = [{"role": "system", "content": "You are a kind helpful assistant."},]
        openai.api_key = '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'

    def chatgpt_answer(self, message):
        QApplication.processEvents()

        print('Passed 2')

        if message:
            self.messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=self.messages
            )
        print('Passed 3')


        reply = chat.choices[0].message.content

        label = QLabel(reply)
        label.setStyleSheet("background-color: rgb(65, 65, 65); "
                            "border: 1px solid rgb(65, 65, 65); "
                            "padding: 3px; "
                            "border-radius:10px; "
                            "border-bottom-left-radius: 0px; "
                            "color: rgb(230, 230, 230);")

        label.setWordWrap(True)
        label.setMaximumWidth(300)

        label.setFixedSize(label.sizeHint())
        label.setMaximumWidth(300)

        # label.setAlignment(Qt.AlignRight)
        self.verticalLayout_6.addWidget(label, 0, Qt.AlignLeft)

        self.messages.append({"role": "assistant", "content": reply})



    def add_label(self):
        text = self.textEdit.toPlainText().strip()

        label = QLabel(text)
        label.setStyleSheet("background-color: #FFFFFF; padding: 6px; border-radius: 4px;")
        label.setWordWrap(True)
        label.setMaximumWidth(300)
        label.setFixedSize(label.sizeHint())
        label.setMaximumWidth(300)

        label.setStyleSheet("background-color: rgb(45, 152, 7);\n"
                                           "border: 1px solid rgb(45, 152, 7);\n"
                                           "padding: 3px;\n"
                                           "border-radius:10px;\n"
                                           "border-bottom-right-radius: 0px;\n"
                                           "")
        # label.setAlignment(Qt.AlignRight)
        self.verticalLayout_6.addWidget(label, 0, Qt.AlignRight)
        QApplication.processEvents()
        time.sleep(0.2)

        print('Passed 1')

        self.chatgpt_answer(text)


        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
        self.textEdit.clear()










import resources_rc
import time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLabel, QScrollArea
from PyQt5.QtCore import Qt
import openai


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
