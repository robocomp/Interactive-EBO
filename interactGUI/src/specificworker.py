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
from fpdf import FPDF
import time
from random import *
import json
#sys.path.insert(0, os.path.join(os.getenv('HOME'), ".learnblock", "clients"))

import pyaudio

from learnbot_dsl.Clients import EBO_sim
from learnbot_dsl.Clients import EBO_remote_sim
from learnbot_dsl.Clients import EBO
from learnbot_dsl.Clients.Client import *


with open('src/frases.json') as file:
    jsonreacciones = json.load(file)

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
sys.path.append('/opt/robocomp/lib')

caracteresaeliminar = [".a", ".m", ".t", ".s"]

# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class SpecificWorker(GenericWorker):
    def __init__(self, proxy_map, startup_check=False):
        super(SpecificWorker, self).__init__(proxy_map)
        self.Period = 200
        if startup_check:
            self.startup_check()
        else:
            self.timer.timeout.connect(self.compute)
            self.timer.start(self.Period)
        self.ui.textoaenviar.returnPressed.connect(self.mandarvoz)
        self.ui.textoescuchado.returnPressed.connect(self.almacenartextoescuchado)
        self.ui.asignarnombre.clicked.connect(self.ponernombre)
        self.ui.limpiarconversacion.clicked.connect(self.vaciarconversacion)
        self.ui.exportarpdf.clicked.connect(self.exportarapdf)
        self.usuario = ""
        self.textograbadoparamostrar = ""
        self.horainicioconversacion = time.strftime("%d-%m-%y_%H-%M-%S")
        self.estructurajson = {}
        self.estructurajson["conversacion"] = []
        self.ui.muestramensajes.setReadOnly(True)
        self.ui.respuesta.setReadOnly(True)
        self.ui.si.clicked.connect(self.afirmacion)
        self.ui.no.clicked.connect(self.negacion)
        self.ui.botonmiedo.clicked.connect(self.estadoMiedo)
        self.ui.botonalegria.clicked.connect(self.estadoAlegre)
        self.ui.botonsorpresa.clicked.connect(self.estadoSorpresa)
        self.ui.botontristeza.clicked.connect(self.estadoTriste)
        self.ui.botonneutral.clicked.connect(self.estadoNeutral)
        self.ui.botondisgustado.clicked.connect(self.estadoDisgustada)
        self.ui.botonenfadado.clicked.connect(self.estadoEnfadada)
        self.ui.mandarfrase.clicked.connect(self.enviarfrasedesplegable)

        self.select_robot()
        self.accionaleatoria = False
        self.estadoactual = "Neutral"
        self.posestadoactual = 4
        self.sec = randint(1, 3)
        self.instlastaction = time.time()
        self.start_time = self.instlastaction
        self.timemax = 1
        self.timemin = 1
        self.velmax = 20
        self.velmin = 20
        self.angmax = 90
        self.angmin = -self.angmax
        self.frecmovementmin = 1
        self.frecmovementmax = 3
        self.actividadaleatoria = False

    def __del__(self):
        print('SpecificWorker destructor')

    def setParams(self, params):
        return True

    @QtCore.Slot()
    def compute(self):

        if (self.ui.comportamientoaleatorio.isChecked() == True):
            if time.time() - self.start_time > self.sec:
                if not self.accionaleatoria:
                    choice([self.randomMovementbackfront(), self.randomMovementrotate()])
                    self.randomMovementrotate()

            if time.time() - self.instlastaction > 10:
                self.accionaleatoria = True
                jsonposition = randint(0, len(jsonreacciones["reacciones"][self.posestadoactual][self.estadoactual]) - 1)
                self.speech_proxy.say(jsonreacciones["reacciones"][self.posestadoactual][self.estadoactual][jsonposition]["frase"], True)
                # self.enviarmovimiento(jsonreacciones["reacciones"][self.estadoactual][jsonposition]["movimiento"])
                self.accionaleatoria = False
                self.instlastaction = time.time()

        if (self.ui.grabar_2.isChecked() == True):
            if(self.textograbadoparamostrar != ""):
               self.ui.respuesta.setPlainText(self.textograbadoparamostrar)
               self.estructurajson["conversacion"].append({'usuario': self.usuario + " (grabado)", 'texto': self.textograbadoparamostrar, "emocionebo": self.estadoactual, 'hora': time.strftime("%H:%M:%S")})
               self.textograbadoparamostrar = ""
        self.textograbadoparamostrar = ""

    def select_robot(self):
        print("Introduce el robot a utilizar: ")
        rob = input()
        if (rob == "sim"):
            try:
                self.robot = EBO_sim.Robot()
            except Exception as e:
                print("Problems creating EBO_sim instance")
                raise (e)
        elif (rob == "remote"):
            try:
                self.robot = EBO_remote_sim.Robot()
            except Exception as e:
                print("Problems creating EBO_remote_sim instance")
                raise (e)
        else:
            try:
                self.robot = EBO.Robot()
            except Exception as e:
                print("Problems creating EBO instance")
                raise (e)

    def startup_check(self):
        QTimer.singleShot(200, QApplication.instance().quit)

    def ponernombre(self):
        self.usuario = self.ui.nombreaintroducir.text()

    def mandarvoz(self):
        print(self.ui.textoaenviar.text())
        saludo = ["¡.aBuenos días, " + self.usuario + "!", "¡.aQue alegría verte, " + self.usuario + "!"]
        despedida = ["¡.aNos vemos pronto, " + self.usuario + "!"]
        if (self.usuario != ""):            
            textoadecir = self.ui.textoaenviar.text()
            self.ui.textoaenviar.clear()
            if(textoadecir.find(":)") != -1):
                textoadecir = random.choice(saludo)
            elif(textoadecir.find(".d") != -1):
                textoadecir = random.choice(despedida)
            try:
                if(textoadecir.find(".m") != -1):
                    self.caraMiedo()
                    self.ui.muestramensajes.setPlainText("Ebo siente miedo.")
                elif(textoadecir.find(".a") != -1):
                    for rep in caracteresaeliminar:
                        textoadecir = textoadecir.replace(rep, "")
                    if (textoadecir != ""):
                        print(textoadecir)
                        self.speech_proxy.say(textoadecir, True)
                        self.estructurajson["conversacion"].append(
                            {'usuario': "Ebo", 'texto': textoadecir, "emocionebo": self.estadoactual,
                                'hora': time.strftime("%H:%M:%S")})
                    self.caraAlegre()
                    self.ui.muestramensajes.setPlainText("¡Ebo está divirtiéndose!.")
                elif(textoadecir.find(".s") != -1):
                    for rep in caracteresaeliminar:
                        textoadecir = textoadecir.replace(rep, "")
                    if(textoadecir != ""):
                        print(textoadecir)
                        self.speech_proxy.say(textoadecir, True)
                        self.estructurajson["conversacion"].append({'usuario': "Ebo", 'texto': textoadecir, "emocionebo": self.estadoactual, 'hora': time.strftime("%H:%M:%S")})
                    self.caraSorpresa()
                    self.ui.muestramensajes.setPlainText("¡Ebo se ha sorprendido!")
                elif(textoadecir.find(".t") != -1):
                    for rep in caracteresaeliminar:
                        textoadecir = textoadecir.replace(rep, "")
                    if(textoadecir != ""):
                        print(textoadecir)
                        self.speech_proxy.say(textoadecir, True)
                        self.estructurajson["conversacion"].append({'usuario': "Ebo", 'texto': textoadecir, "emocionebo": self.estadoactual, 'hora': time.strftime("%H:%M:%S")})
                    self.caraTriste()
                    self.ui.muestramensajes.setPlainText("Ebo está triste.")
                else:
                    for rep in caracteresaeliminar:
                        textoadecir = textoadecir.replace(rep, "")
                    if(textoadecir != ""):
                        print(textoadecir)
                        self.speech_proxy.say(textoadecir, True)
                        self.estructurajson["conversacion"].append({'usuario': "Ebo", 'texto': textoadecir, "emocionebo": self.estadoactual, 'hora': time.strftime("%H:%M:%S")})
            except:
                print("Error")
        else:
            self.ui.muestramensajes.setPlainText("Se necesita un nombre de usuario.")
            self.ui.textoaenviar.clear()
        self.instlastaction = time.time()

    def enviarfrasedesplegable(self):
        textoadecir = self.ui.frasesPredefinidas.currentText()
        print(textoadecir)
        self.speech_proxy.say(textoadecir, True)
        self.estructurajson["conversacion"].append({'usuario': "Ebo", 'texto': textoadecir, "emocionebo": self.estadoactual, 'hora': time.strftime("%H:%M:%S")})

    def exportarapdf(self):
        if (self.usuario != ""):
            iterador = 3
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=15)
            pdf.cell(200, 10, txt=self.usuario + " " + self.horainicioconversacion, ln=1, align='C')
            # with open("../" + name + "_" + self.horainicioconversacion + ".json", "w") as ficherosalida:
            #    json.dump(self.estructurajson, ficherosalida)
            for p in self.estructurajson["conversacion"]:
                pdf.multi_cell(180, 10, txt=p["hora"] + " " + p["usuario"] + " " + p["emocionebo"] + " -> " + p['texto'], border = 0, align='J', fill = False)
                pdf.ln()
                iterador += 1
            pdf.output(self.usuario + "_" + self.horainicioconversacion + ".pdf")
            self.ui.muestramensajes.setPlainText("Se ha exportado correctamente")
        else:
            self.ui.muestramensajes.setPlainText("Se necesita un nombre de usuario.")

    def vaciarconversacion(self):
        self.estructurajson = {}
        self.estructurajson["conversacion"] = []
        self.ui.muestramensajes.setPlainText("Se ha limpiado la conversación.")

    def almacenartextoescuchado(self):
        if (self.usuario != ""):
            escucha = self.ui.textoescuchado.text()
            self.estructurajson["conversacion"].append({'usuario': self.usuario + " (escrito)", 'texto': escucha, "emocionebo": self.estadoactual, 'hora': time.strftime("%H:%M:%S")})
        else:
            self.ui.muestramensajes.setPlainText("Se necesita un nombre de usuario.")
        self.ui.textoescuchado.clear()

    # def strtoface(self, strface):
    #     if(strface == "Triste"):
    #         self.caraTriste()
    #     elif(strface == "Alegre"):
    #         self.caraAlegre()
    #     elif (strface == "Enfadada"):
    #         self.caraEnfadada()
    #     elif (strface == "Neutral"):
    #         self.caraNeutral()
    #     elif (strface == "Disgustada"):
    #         self.caraDisgustada()
    #     elif (strface == "Sorpresa"):
    #         self.caraSorpresa()
    #     else:
    #         self.caraMiedo()

    def enviarmovimiento(self, mov):
        if mov == "Rotacion":
            tact = time.time()
            while (time.time() <= tact + 5):
                self.robot.setBaseSpeed(150, 90)
            self.robot.setBaseSpeed(0, 0)
        elif mov == "BackFront":
            tact = time.time()
            while (time.time() <= tact + 0.05):
                self.robot.setBaseSpeed(150, 0)
            tact = time.time()
            while (time.time() <= tact + 0.1):
                self.robot.setBaseSpeed(-150, 0)
            tact = time.time()
            while (time.time() <= tact + 0.1):
                self.robot.setBaseSpeed(150, 0)
            tact = time.time()
            while (time.time() <= tact + 0.1):
                self.robot.setBaseSpeed(-150, 0)
            tact = time.time()
            while (time.time() <= tact + 0.05):
                self.robot.setBaseSpeed(150, 0)
            self.robot.setBaseSpeed(0, 0)

    def estadoTriste(self):
        self.robot.express(Emotions.Sadness)
        self.estadoactual = "Triste"
        self.posestadoactual = 3
        self.instlastaction = time.time()
        self.timemax = 0.9
        self.timemin = 1.2
        self.velmax = 10
        self.velmin = 1
        self.frecmovementmin = 4
        self.frecmovementmax = 8
        self.angmax = 30
        self.speech_proxy.setVoice(self.estadoactual)

    def estadoAlegre(self):
        self.robot.express(Emotions.Joy)
        self.estadoactual = "Alegre"
        self.posestadoactual = 0
        self.instlastaction = time.time()
        self.timemax = 0.15
        self.timemin = 0.3
        self.velmax = 140
        self.velmin = 100
        self.frecmovementmin = 1
        self.frecmovementmax = 3
        self.angmax = 60
        self.speech_proxy.setVoice(self.estadoactual)

    def estadoEnfadada(self):
        self.robot.express(Emotions.Anger)
        self.estadoactual = "Enfadada"
        self.posestadoactual = 1
        self.instlastaction = time.time()
        self.timemax = 0.3
        self.timemin = 0.15
        self.velmax = 140
        self.velmin = 100
        self.frecmovementmin = 0.2
        self.frecmovementmax = 2
        self.angmax = 90
        self.speech_proxy.setVoice(self.estadoactual)

    def estadoNeutral(self):
        self.robot.express(Emotions.Neutral)
        self.estadoactual = "Neutral"
        self.posestadoactual = 4
        self.instlastaction = time.time()
        self.timemax = 0.3
        self.timemin = 0.15
        self.velmax = 80
        self.velmin = 60
        self.frecmovementmin = 2
        self.frecmovementmax = 4
        self.angmax = 90
        self.speech_proxy.setVoice(self.estadoactual)

    def estadoDisgustada(self):
        self.robot.express(Emotions.Disgust)
        self.estadoactual = "Disgustada"
        self.posestadoactual = 2
        self.instlastaction = time.time()
        self.timemax = 0.7
        self.timemin = 1
        self.velmax = 40
        self.velmin = 20
        self.frecmovementmin = 4
        self.frecmovementmax = 8
        self.angmax = 30
        self.speech_proxy.setVoice(self.estadoactual)

    def estadoSorpresa(self):
        self.robot.express(Emotions.Surprise)
        self.estadoactual = "Sorpresa"
        self.posestadoactual = 5
        self.instlastaction = time.time()
        self.timemax = 0.3
        self.timemin = 0.15
        self.velmax = 80
        self.velmin = 60
        self.frecmovementmin = 1
        self.frecmovementmax = 2
        self.angmax = 50
        self.speech_proxy.setVoice(self.estadoactual)

    def estadoMiedo(self):
        self.robot.express(Emotions.Fear)
        self.estadoactual = "Miedo"
        self.posestadoactual = 6
        self.instlastaction = time.time()
        self.timemax = 0.2
        self.timemin = 0.15
        self.velmax = 80
        self.velmin = 60
        self.frecmovementmin = 0.3
        self.frecmovementmax = 1
        self.angmax = 120
        self.speech_proxy.setVoice(self.estadoactual)

    # def movimientoMiedo(self):
    #     tact = time.time()
    #     while (time.time() <= tact + 0.25):
    #         self.robot.setBaseSpeed(-100, -15)
    #     tact = time.time()
    #     while (time.time() <= tact + 0.25):
    #         self.robot.setBaseSpeed(-100, 15)
    #     self.robot.setBaseSpeed(0, 0)
    #     self.instlastaction = time.time()
    #
    # def movimientoAlegria(self):
    #     tact = time.time()
    #     while (time.time() <= tact + 0.25):
    #         self.robot.setBaseSpeed(100, -15)
    #     tact = time.time()
    #     while (time.time() <= tact + 0.25):
    #         self.robot.setBaseSpeed(100, 15)
    #     tact = time.time()
    #     while (time.time() <= tact + 0.25):
    #         self.robot.setBaseSpeed(-100, -15)
    #     tact = time.time()
    #     while (time.time() <= tact + 0.25):
    #         self.robot.setBaseSpeed(-100, 15)
    #     self.robot.setBaseSpeed(0,0)
    #     self.instlastaction = time.time()

    def afirmacion(self):
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 0)
        tact = time.time()
        while (time.time() <= tact + 0.3):
            self.robot.setBaseSpeed(-100, 0)
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 0)
        self.robot.setBaseSpeed(0, 0)
        self.instlastaction = time.time()

    def negacion(self):
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 90)
        tact = time.time()
        while (time.time() <= tact + 0.3):
            self.robot.setBaseSpeed(100, -90)
        tact = time.time()
        while (time.time() <= tact + 0.15):
            self.robot.setBaseSpeed(100, 90)
        self.robot.setBaseSpeed(0,0)
        self.instlastaction = time.time()

    def newText(self, text):
        self.textograbadoparamostrar = text

    def randomMovementrotate(self):
        tact = time.time()
        randomtime = uniform(self.timemin, self.timemax)
        speed = randint(self.velmin, self.velmax)
        angle = randint(self.angmin, self.angmax)
        while (time.time() <= tact + randomtime):
            self.robot.setBaseSpeed(speed, angle)
        tact = time.time()
        while (time.time() <= tact + randomtime):
            self.robot.setBaseSpeed(-speed, angle)
        self.robot.setBaseSpeed(0, 0)
        self.start_time = time.time()
        self.sec = uniform(self.frecmovementmin, self.frecmovementmax)

    def randomMovementbackfront(self):
        tact = time.time()
        randomtime = uniform(self.timemin, self.timemax)
        speed = randint(self.velmin, self.velmax)
        while (time.time() <= tact + randomtime):
            self.robot.setBaseSpeed(speed, 0)
            self.robot.setBaseSpeed(-speed, 0)
        self.robot.setBaseSpeed(0, 0)
        self.start_time = time.time()
        self.sec = uniform(self.frecmovementmin, self.frecmovementmax)


