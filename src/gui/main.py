import sys
from PySide6 import QtCore, QtGui
from PySide6.QtCore import (QPropertyAnimation)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main_window import Ui_MainWindow

from functools import partial

SHOW_MAXIMIZED = True


def slideFrame(frame, slideAnimation):
    isSlided = False
    afterAnimationHeight = None
    actualHeight = None

    print("xd ", frame.height())

    if frame.height() == 120:  # height before slide
        isSlided = False
        afterAnimationHeight = 300
        actualHeight = 120
        print("tr")
    else:  # frame.height() == 300: # after slide
        isSlided = True
        afterAnimationHeight = 120
        actualHeight = 300
        print("fa")

    print(frame)

    slideAnimation = QPropertyAnimation(frame, b'minimumHeight')
    slideAnimation.setDuration(450)
    slideAnimation.setStartValue(actualHeight)
    slideAnimation.setEndValue(afterAnimationHeight)
    slideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    slideAnimation.start()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.closeButton.clicked.connect(self.close)
        self.ui.minimizeButton.clicked.connect(self.showMinimized())
        self.ui.restoreButton.clicked.connect(self.restore)

        self.tables = [self.ui.tableRent, self.ui.tableCredit, self.ui.tableInformation,
                       self.ui.tableMainCharacteristics, self.ui.tableOwnContribution,
                       self.ui.tableInvestmentAssessment]

        self.frameHeight = 80
        self.targetFrameHeight = 300

        self.decreaseFrameHeights(80)

        # animation section
        self.mainCharacteristicsSlideAnimation = None
        self.ui.button_main_characteristics.clicked.connect(self.slideMainCharacteristics)
        self.informationSlideAnimation = None
        self.ui.button_information.clicked.connect(self.slideInformation)
        self.creditSlideAnimation = None
        self.ui.button_credit.clicked.connect(self.slideCredit)
        self.rentSlideAnimation = None
        self.ui.button_rent.clicked.connect(self.slideRent)
        self.investmentAssessmentSlideAnimation = None
        self.ui.button_investment_assessment.clicked.connect(self.slideInvestmentAssessment)
        self.ownContributionSlideAnimation = None
        self.ui.button_own_contribution.clicked.connect(self.slideOwnContribution)

        self.showFullScreen()
        self.show()

        print(self.ui.frame_main_characteristics.size())
        print(self.ui.frame_information.size())

    def decreaseFrameHeights(self, minHeight):
        self.ui.frame_information.resize(self.ui.frame_information.width(), minHeight)
        self.ui.frame_main_characteristics.resize(self.ui.frame_main_characteristics.width(), minHeight)
        self.ui.frame_rent.resize(self.ui.frame_rent.width(), minHeight)
        self.ui.frame_credit.resize(self.ui.frame_credit.width(), minHeight)
        self.ui.frame_own_contribution.resize(self.ui.frame_own_contribution.width(), minHeight)
        self.ui.frame_investment_assessment.resize(self.ui.frame_investment_assessment.width(), minHeight)

        for table in self.tables:
            table.setVisible(False)

        # self.ui.frame_main_characteristics.setMinimumHeight(minHeight)
        # self.ui.frame_information.setMinimumHeight(minHeight)
        # self.ui.frame_credit.setMinimumHeight(minHeight)
        # self.ui.frame_investment_assessment.setMinimumHeight(minHeight)
        # self.ui.frame_rent.setMinimumHeight(minHeight)
        # self.ui.frame_own_contribution.setMinimumHeight(minHeight)

    def slideMainCharacteristics(self):

        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_main_characteristics.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 300
            actualHeight = self.frameHeight
            self.ui.tableMainCharacteristics.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 300
            self.ui.tableMainCharacteristics.setVisible(False)

        self.mainCharacteristicsSlideAnimation = QPropertyAnimation(self.ui.frame_main_characteristics,
                                                                    b'minimumHeight')
        self.mainCharacteristicsSlideAnimation.setDuration(450)
        self.mainCharacteristicsSlideAnimation.setStartValue(actualHeight)
        self.mainCharacteristicsSlideAnimation.setEndValue(afterAnimationHeight)
        self.mainCharacteristicsSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.mainCharacteristicsSlideAnimation.start()



    def slideInformation(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_information.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 300
            actualHeight = self.frameHeight
            self.ui.tableInformation.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 300
            self.ui.tableInformation.setVisible(False)

        self.informationSlideAnimation = QPropertyAnimation(self.ui.frame_information,
                                                                    b'minimumHeight')
        self.informationSlideAnimation.setDuration(450)
        self.informationSlideAnimation.setStartValue(actualHeight)
        self.informationSlideAnimation.setEndValue(afterAnimationHeight)
        self.informationSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.informationSlideAnimation.start()

    def slideCredit(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_credit.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 300
            actualHeight = self.frameHeight
            self.ui.tableCredit.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 300
            self.ui.tableCredit.setVisible(False)

        self.creditSlideAnimation = QPropertyAnimation(self.ui.frame_credit,
                                                       b'minimumHeight')
        self.creditSlideAnimation.setDuration(450)
        self.creditSlideAnimation.setStartValue(actualHeight)
        self.creditSlideAnimation.setEndValue(afterAnimationHeight)
        self.creditSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.creditSlideAnimation.start()

    def slideRent(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_rent.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 300
            actualHeight = self.frameHeight
            self.ui.tableRent.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 300
            self.ui.tableRent.setVisible(False)

        self.rentSlideAnimation = QPropertyAnimation(self.ui.frame_rent,
                                                     b'minimumHeight')
        self.rentSlideAnimation.setDuration(450)
        self.rentSlideAnimation.setStartValue(actualHeight)
        self.rentSlideAnimation.setEndValue(afterAnimationHeight)
        self.rentSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.rentSlideAnimation.start()

    def slideInvestmentAssessment(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_investment_assessment.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 300
            actualHeight = self.frameHeight
            self.ui.tableInvestmentAssessment.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 300
            self.ui.tableInvestmentAssessment.setVisible(False)

        self.investmentAssessmentSlideAnimation = QPropertyAnimation(self.ui.frame_investment_assessment,
                                                                    b'minimumHeight')
        self.investmentAssessmentSlideAnimation.setDuration(450)
        self.investmentAssessmentSlideAnimation.setStartValue(actualHeight)
        self.investmentAssessmentSlideAnimation.setEndValue(afterAnimationHeight)
        self.investmentAssessmentSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.investmentAssessmentSlideAnimation.start()

    def slideOwnContribution(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_own_contribution.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 300
            actualHeight = self.frameHeight
            self.ui.tableOwnContribution.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 300
            self.ui.tableOwnContribution.setVisible(False)

        self.ownContributionSlideAnimation = QPropertyAnimation(self.ui.frame_own_contribution,
                                                                    b'minimumHeight')
        self.ownContributionSlideAnimation.setDuration(450)
        self.ownContributionSlideAnimation.setStartValue(actualHeight)
        self.ownContributionSlideAnimation.setEndValue(afterAnimationHeight)
        self.ownContributionSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.ownContributionSlideAnimation.start()

    def restore(self):
        global SHOW_MAXIMIZED
        if SHOW_MAXIMIZED:
            SHOW_MAXIMIZED = False
            self.showNormal()
        else:
            SHOW_MAXIMIZED = True
            self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
