# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'needs_manager_dialog_base.ui'
#
# Created: Thu Nov 27 10:02:27 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NeedsManagerDialogBase(object):
    def setupUi(self, NeedsManagerDialogBase):
        NeedsManagerDialogBase.setObjectName(_fromUtf8("NeedsManagerDialogBase"))
        NeedsManagerDialogBase.resize(751, 669)
        NeedsManagerDialogBase.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.gridLayout_2 = QtGui.QGridLayout(NeedsManagerDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontal_layout = QtGui.QHBoxLayout()
        self.horizontal_layout.setObjectName(_fromUtf8("horizontal_layout"))
        self.profileLabel = QtGui.QLabel(NeedsManagerDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileLabel.sizePolicy().hasHeightForWidth())
        self.profileLabel.setSizePolicy(sizePolicy)
        self.profileLabel.setObjectName(_fromUtf8("profileLabel"))
        self.horizontal_layout.addWidget(self.profileLabel)
        self.profile_combo = QtGui.QComboBox(NeedsManagerDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_combo.sizePolicy().hasHeightForWidth())
        self.profile_combo.setSizePolicy(sizePolicy)
        self.profile_combo.setObjectName(_fromUtf8("profile_combo"))
        self.horizontal_layout.addWidget(self.profile_combo)
        self.remove_profile_button = QtGui.QPushButton(NeedsManagerDialogBase)
        self.remove_profile_button.setObjectName(_fromUtf8("remove_profile_button"))
        self.horizontal_layout.addWidget(self.remove_profile_button)
        self.gridLayout_2.addLayout(self.horizontal_layout, 0, 0, 1, 1)
        self.stacked_widget = QtGui.QStackedWidget(NeedsManagerDialogBase)
        self.stacked_widget.setEnabled(True)
        self.stacked_widget.setMouseTracking(False)
        self.stacked_widget.setFrameShape(QtGui.QFrame.NoFrame)
        self.stacked_widget.setFrameShadow(QtGui.QFrame.Plain)
        self.stacked_widget.setLineWidth(0)
        self.stacked_widget.setObjectName(_fromUtf8("stacked_widget"))
        self.profile_edit_page = QtGui.QWidget()
        self.profile_edit_page.setObjectName(_fromUtf8("profile_edit_page"))
        self.gridLayout_3 = QtGui.QGridLayout(self.profile_edit_page)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.profile_edit_page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(437, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.add_resource_button = QtGui.QPushButton(self.profile_edit_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_resource_button.sizePolicy().hasHeightForWidth())
        self.add_resource_button.setSizePolicy(sizePolicy)
        self.add_resource_button.setMaximumSize(QtCore.QSize(32, 32))
        self.add_resource_button.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.add_resource_button.setFont(font)
        self.add_resource_button.setAutoFillBackground(False)
        self.add_resource_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/add_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_resource_button.setIcon(icon)
        self.add_resource_button.setCheckable(False)
        self.add_resource_button.setAutoDefault(True)
        self.add_resource_button.setDefault(False)
        self.add_resource_button.setFlat(False)
        self.add_resource_button.setObjectName(_fromUtf8("add_resource_button"))
        self.gridLayout_3.addWidget(self.add_resource_button, 0, 3, 1, 1)
        self.remove_resource_button = QtGui.QPushButton(self.profile_edit_page)
        self.remove_resource_button.setMaximumSize(QtCore.QSize(32, 32))
        self.remove_resource_button.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.remove_resource_button.setFont(font)
        self.remove_resource_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/remove_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_resource_button.setIcon(icon1)
        self.remove_resource_button.setObjectName(_fromUtf8("remove_resource_button"))
        self.gridLayout_3.addWidget(self.remove_resource_button, 0, 4, 1, 1)
        self.edit_resource_button = QtGui.QPushButton(self.profile_edit_page)
        self.edit_resource_button.setMaximumSize(QtCore.QSize(32, 32))
        self.edit_resource_button.setBaseSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.edit_resource_button.setFont(font)
        self.edit_resource_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/edit_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_resource_button.setIcon(icon2)
        self.edit_resource_button.setObjectName(_fromUtf8("edit_resource_button"))
        self.gridLayout_3.addWidget(self.edit_resource_button, 0, 5, 1, 1)
        self.resources_list = QtGui.QListWidget(self.profile_edit_page)
        self.resources_list.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.resources_list.setAlternatingRowColors(True)
        self.resources_list.setWordWrap(True)
        self.resources_list.setObjectName(_fromUtf8("resources_list"))
        self.gridLayout_3.addWidget(self.resources_list, 1, 0, 1, 6)
        self.provenance_label = QtGui.QLabel(self.profile_edit_page)
        self.provenance_label.setObjectName(_fromUtf8("provenance_label"))
        self.gridLayout_3.addWidget(self.provenance_label, 2, 0, 1, 1)
        self.provenance = QtGui.QLineEdit(self.profile_edit_page)
        self.provenance.setObjectName(_fromUtf8("provenance"))
        self.gridLayout_3.addWidget(self.provenance, 2, 1, 1, 5)
        self.stacked_widget.addWidget(self.profile_edit_page)
        self.resource_edit_page = QtGui.QWidget()
        self.resource_edit_page.setObjectName(_fromUtf8("resource_edit_page"))
        self.gridLayout = QtGui.QGridLayout(self.resource_edit_page)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.resource_widget = QtGui.QWidget(self.resource_edit_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resource_widget.sizePolicy().hasHeightForWidth())
        self.resource_widget.setSizePolicy(sizePolicy)
        self.resource_widget.setObjectName(_fromUtf8("resource_widget"))
        self.gridLayout.addWidget(self.resource_widget, 1, 0, 1, 2)
        self.resource_editor_label = QtGui.QLabel(self.resource_edit_page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resource_editor_label.setFont(font)
        self.resource_editor_label.setObjectName(_fromUtf8("resource_editor_label"))
        self.gridLayout.addWidget(self.resource_editor_label, 0, 0, 1, 1)
        self.stacked_widget.addWidget(self.resource_edit_page)
        self.gridLayout_2.addWidget(self.stacked_widget, 1, 0, 1, 1)
        self.button_box = QtGui.QDialogButtonBox(NeedsManagerDialogBase)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout_2.addWidget(self.button_box, 2, 0, 1, 1)

        self.retranslateUi(NeedsManagerDialogBase)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), NeedsManagerDialogBase.reject)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), NeedsManagerDialogBase.accept)
        QtCore.QMetaObject.connectSlotsByName(NeedsManagerDialogBase)

    def retranslateUi(self, NeedsManagerDialogBase):
        NeedsManagerDialogBase.setWindowTitle(_translate("NeedsManagerDialogBase", "Minimum Needs Manager", None))
        self.profileLabel.setText(_translate("NeedsManagerDialogBase", "Profile", None))
        self.profile_combo.setToolTip(_translate("NeedsManagerDialogBase", "Select a profile", None))
        self.remove_profile_button.setText(_translate("NeedsManagerDialogBase", "Remove", None))
        self.label.setText(_translate("NeedsManagerDialogBase", "Resources for this profile", None))
        self.add_resource_button.setToolTip(_translate("NeedsManagerDialogBase", "Add new resource", None))
        self.remove_resource_button.setToolTip(_translate("NeedsManagerDialogBase", "Remove selected resource", None))
        self.edit_resource_button.setToolTip(_translate("NeedsManagerDialogBase", "Edit selected resource", None))
        self.provenance_label.setText(_translate("NeedsManagerDialogBase", "Provenance", None))
        self.resource_editor_label.setText(_translate("NeedsManagerDialogBase", "Resource editor", None))

import resources_rc
