#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2021 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication
from genericworker import *
import pyaudio
import speech_recognition as sr
import time

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map, startup_check=False):
        super(SpecificWorker, self).__init__(proxy_map)
        self.Period = 2000
        if startup_check:
            self.startup_check()
        else:
            self.timer.timeout.connect(self.compute)
            self.timer.start(self.Period)

    def __del__(self):
        print('SpecificWorker destructor')

    def setParams(self, params):

        return True

    @QtCore.Slot()
    def compute(self):

        r = sr.Recognizer()
        with sr.Microphone(device_index=0) as source:
            print('Please start speaking..\n')
            audio2 = r.listen(source, 3)
            try:
                text = r.recognize_google(audio2, language="es-ES")
                print(text)
                self.asrpublish_proxy.newText(text)
            except Exception as e:
                print("Problems with recognize_google")


    def startup_check(self):
        QTimer.singleShot(200, QApplication.instance().quit)




    ######################
    # From the RoboCompASRPublish you can publish calling this methods:
    # self.asrpublish_proxy.newText(...)

