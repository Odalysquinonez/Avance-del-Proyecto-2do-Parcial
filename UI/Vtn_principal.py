# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_VTNWindow(object):
    def setupUi(self, VTNWindow):
        if not VTNWindow.objectName():
            VTNWindow.setObjectName(u"VTNWindow")
        VTNWindow.resize(465, 284)
        self.centralwidet = QWidget(VTNWindow)
        self.centralwidet.setObjectName(u"centralwidet")
        self.txt_Nombre = QLineEdit(self.centralwidet)
        self.txt_Nombre.setObjectName(u"txt_Nombre")
        self.txt_Nombre.setGeometry(QRect(130, 40, 141, 31))
        self.txt_Nombre.setMaxLength(50)
        self.txt_Apellido = QLineEdit(self.centralwidet)
        self.txt_Apellido.setObjectName(u"txt_Apellido")
        self.txt_Apellido.setGeometry(QRect(130, 80, 141, 31))
        self.txt_Apellido.setMaxLength(50)
        self.lbl_Nombre = QLabel(self.centralwidet)
        self.lbl_Nombre.setObjectName(u"lbl_Nombre")
        self.lbl_Nombre.setGeometry(QRect(40, 40, 81, 21))
        self.lbl_Apellido = QLabel(self.centralwidet)
        self.lbl_Apellido.setObjectName(u"lbl_Apellido")
        self.lbl_Apellido.setGeometry(QRect(40, 80, 61, 21))
        self.btn_Grabar = QPushButton(self.centralwidet)
        self.btn_Grabar.setObjectName(u"btn_Grabar")
        self.btn_Grabar.setGeometry(QRect(150, 220, 81, 21))
        self.cb_tipo_persona = QComboBox(self.centralwidet)
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.addItem("")
        self.cb_tipo_persona.setObjectName(u"cb_tipo_persona")
        self.cb_tipo_persona.setGeometry(QRect(130, 10, 141, 21))
        self.lbl_tipo_persona = QLabel(self.centralwidet)
        self.lbl_tipo_persona.setObjectName(u"lbl_tipo_persona")
        self.lbl_tipo_persona.setGeometry(QRect(20, 10, 91, 21))
        self.txt_Nombre_2 = QLineEdit(self.centralwidet)
        self.txt_Nombre_2.setObjectName(u"txt_Nombre_2")
        self.txt_Nombre_2.setGeometry(QRect(130, 160, 141, 31))
        self.txt_cedula = QLineEdit(self.centralwidet)
        self.txt_cedula.setObjectName(u"txt_cedula")
        self.txt_cedula.setGeometry(QRect(130, 120, 141, 31))
        self.txt_cedula.setMaxLength(10)
        self.txt_email = QLineEdit(self.centralwidet)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(130, 160, 141, 31))
        self.txt_email.setMaxLength(100)
        self.lbl_cedula = QLabel(self.centralwidet)
        self.lbl_cedula.setObjectName(u"lbl_cedula")
        self.lbl_cedula.setGeometry(QRect(40, 130, 81, 21))
        self.lbl_email = QLabel(self.centralwidet)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setGeometry(QRect(40, 170, 61, 21))
        self.btn_buscar_cedula = QPushButton(self.centralwidet)
        self.btn_buscar_cedula.setObjectName(u"btn_buscar_cedula")
        self.btn_buscar_cedula.setGeometry(QRect(290, 90, 111, 21))
        VTNWindow.setCentralWidget(self.centralwidet)
        self.mnb_menu_principal = QMenuBar(VTNWindow)
        self.mnb_menu_principal.setObjectName(u"mnb_menu_principal")
        self.mnb_menu_principal.setGeometry(QRect(0, 0, 465, 21))
        VTNWindow.setMenuBar(self.mnb_menu_principal)
        self.stb_menu_barra_estado = QStatusBar(VTNWindow)
        self.stb_menu_barra_estado.setObjectName(u"stb_menu_barra_estado")
        VTNWindow.setStatusBar(self.stb_menu_barra_estado)

        self.retranslateUi(VTNWindow)

        QMetaObject.connectSlotsByName(VTNWindow)
    # setupUi

    def retranslateUi(self, VTNWindow):
        VTNWindow.setWindowTitle(QCoreApplication.translate("VTNWindow", u"VentanaPrincipal", None))
        self.lbl_Nombre.setText(QCoreApplication.translate("VTNWindow", u"Nombre:", None))
        self.lbl_Apellido.setText(QCoreApplication.translate("VTNWindow", u"Apellido:", None))
        self.btn_Grabar.setText(QCoreApplication.translate("VTNWindow", u"Grabar", None))
        self.cb_tipo_persona.setItemText(0, QCoreApplication.translate("VTNWindow", u"Docente", None))
        self.cb_tipo_persona.setItemText(1, QCoreApplication.translate("VTNWindow", u"Estudiante", None))

        self.lbl_tipo_persona.setText(QCoreApplication.translate("VTNWindow", u"Tipo de Persona", None))
        self.lbl_cedula.setText(QCoreApplication.translate("VTNWindow", u"C\u00e9dula:", None))
        self.lbl_email.setText(QCoreApplication.translate("VTNWindow", u"Email:", None))
        self.btn_buscar_cedula.setText(QCoreApplication.translate("VTNWindow", u"Buscar por cedula", None))
    # retranslateUi

