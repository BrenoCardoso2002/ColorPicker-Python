# Importações:
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QSlider, QSpinBox, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

# Classe da Janela:
class Janela(QWidget):
    def __init__(self):
        super(Janela, self).__init__()

        # Propriedades da Janela:
        self.topo = 512
        self.esquerda = 512
        self.largura = 425
        self.altura = 256
        self.titulo = "Seletor de Cor"
        self.setFixedSize(self.largura, self.altura)

        # Tela em branco:
        self.setStyleSheet("background-color: white;")

        # Label (titulo):
        Label1 = QLabel(self)
        Label1.move(90, 10)
        Label1.setText(self.titulo)
        Label1.setStyleSheet('QLabel {font-size: 26px; color: black; font-weight: bold;}')

        # QPushButton (Cor selecionada):
        self.SelectedCor = QPushButton(self)
        self.SelectedCor.move(275, 15)
        self.SelectedCor.resize(25, 25)
        self.SelectedCor.setStyleSheet('QPushButton {background: black;}')
        self.SelectedCor.setEnabled(False)

        # Label (red):
        Label2 = QLabel(self)
        Label2.move(20, 45)
        Label2.setText("RED")
        Label2.setStyleSheet('QLabel {font-size: 22px; color: red; font-weight: bold;}')

        # Slider (red):
        self.sliderRed = QSlider(Qt.Orientation.Horizontal, self)
        self.sliderRed.move(75, 42)
        self.sliderRed.setRange(0, 255)
        self.sliderRed.setValue(0)
        self.sliderRed.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.sliderRed.resize(250, 25)
        self.sliderRed.setStyleSheet(""" QSlider { background: transparent; } """)
        self.sliderRed.valueChanged.connect(self.changedSliderRed)

        # SpinBox (red):
        self.spinRed = QSpinBox(self)
        self.spinRed.move(330, 40)
        self.spinRed.setRange(0, 255)
        self.spinRed.setValue(0)
        self.spinRed.setSingleStep(1)
        self.spinRed.resize(60, 35)
        self.spinRed.setStyleSheet('QSpinBox {font-size: 20px; color: red;}')
        self.spinRed.valueChanged.connect(self.changedSpinRed)

        # Label (green):
        Label3 = QLabel(self)
        Label3.move(20, 85)
        Label3.setText("Green")
        Label3.setStyleSheet('QLabel {font-size: 22px; color: green; font-weight: bold;}')

        # Slider (green):
        self.sliderGreen = QSlider(Qt.Orientation.Horizontal, self)
        self.sliderGreen.move(95, 82)
        self.sliderGreen.setRange(0, 255)
        self.sliderGreen.setValue(0)
        self.sliderGreen.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.sliderGreen.resize(250, 25)
        self.sliderGreen.setStyleSheet(""" QSlider { background: transparent; } """)
        self.sliderGreen.valueChanged.connect(self.changedSliderGreen)

        # SpinBox (green):
        self.spinGreen = QSpinBox(self)
        self.spinGreen.move(350, 80)
        self.spinGreen.setRange(0, 255)
        self.spinGreen.setValue(0)
        self.spinGreen.setSingleStep(1)
        self.spinGreen.resize(60, 35)
        self.spinGreen.setStyleSheet('QSpinBox {font-size: 20px; color: green;}')
        self.spinGreen.valueChanged.connect(self.changedSpinGreen)

        # Label (blue):
        Label4 = QLabel(self)
        Label4.move(20, 125)
        Label4.setText("Blue")
        Label4.setStyleSheet('QLabel {font-size: 22px; color: blue; font-weight: bold;}')

        # Slider (blue):
        self.sliderBlue = QSlider(Qt.Orientation.Horizontal, self)
        self.sliderBlue.move(80, 122)
        self.sliderBlue.setRange(0, 255)
        self.sliderBlue.setValue(0)
        self.sliderBlue.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.sliderBlue.resize(250, 25)
        self.sliderBlue.setStyleSheet(""" QSlider { background: transparent; } """)
        self.sliderBlue.valueChanged.connect(self.changedSliderBlue)

        # SpinBox (blue):
        self.spinBlue = QSpinBox(self)
        self.spinBlue.move(335, 120)
        self.spinBlue.setRange(0, 255)
        self.spinBlue.setValue(0)
        self.spinBlue.setSingleStep(1)
        self.spinBlue.resize(60, 35)
        self.spinBlue.setStyleSheet('QSpinBox {font-size: 20px; color: blue;}')
        self.spinBlue.valueChanged.connect(self.changedSpinBlue)

        # Label (RGB CODE):
        Label5 = QLabel(self)
        Label5.move(15, 175)
        Label5.setText("RGB Code:")
        Label5.setStyleSheet('QLabel {font-size: 22px; color: black; font-weight: bold;}')

        # QLineEdit(RGB):
        self.txtRGB = QLineEdit(self)
        self.txtRGB.move(130, 175)
        self.txtRGB.resize(190, 30)
        self.txtRGB.setStyleSheet('QLineEdit {font: bold; font-size: 20px; color: black}')
        self.txtRGB.setEnabled(False)
        self.txtRGB.setText("RGB (000, 000, 000)")
        
        # QPuhButton (RGB)
        CopyRGB = QPushButton(self)
        CopyRGB.move(325, 180)
        CopyRGB.setText("Copiar RGB")
        CopyRGB.setStyleSheet('QPushButton {font: normal; font-size: 14px; color: black} QPushButton::pressed {font: bold; font-size: 14px; color: #4a235a ;}')
        CopyRGB.clicked.connect(self.copyRGB)


        # Label (HEX CODE):
        Label6 = QLabel(self)
        Label6.move(35, 210)
        Label6.setText("HEX Code:")
        Label6.setStyleSheet('QLabel {font-size: 22px; color: black; font-weight: bold;}')

        # QLineEdit(HEX):
        self.txtHEX = QLineEdit(self)
        self.txtHEX.move(155, 215)
        self.txtHEX.resize(100, 30)
        self.txtHEX.setStyleSheet('QLineEdit {font: bold; font-size: 20px; color: black}')
        self.txtHEX.setEnabled(False)
        self.txtHEX.setText("#000000")
        
        # QPuhButton (HEX)
        CopyHEX = QPushButton(self)
        CopyHEX.move(260, 220)
        CopyHEX.setText("Copiar HEX")
        CopyHEX.setStyleSheet('QPushButton {font: normal; font-size: 14px; color: black;} QPushButton::pressed {font: bold; font-size: 14px; color: #4a235a;}')
        CopyHEX.clicked.connect(self.copyHEX)

        # Abre a janela:
        self.LoadJanela()

        # Função que carrega a janela:
    def LoadJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    # ChangedEvent (Red Slider)
    def changedSliderRed(self):
        value = self.sliderRed.value() # Obtem o valor que está no slider
        self.spinRed.setValue(value) # define o valor da slider no spin
        self.rgbCODE()
        self.hexCODE()        
    
    # ChangedEvent (Red Spin)
    def changedSpinRed(self):
        value = self.spinRed.value() # Obtem o valor que está no spin
        self.sliderRed.setValue(value) # define o valor da spin no slider
    
    # ChangedEvent (Green Slider)
    def changedSliderGreen(self):
        value = self.sliderGreen.value() # Obtem o valor que está no slider
        self.spinGreen.setValue(value) # define o valor da slider no spin
        self.rgbCODE()
        self.hexCODE()   
    
    # ChangedEvent (Green Spin)
    def changedSpinGreen(self):
        value = self.spinGreen.value() # Obtem o valor que está no spin
        self.sliderGreen.setValue(value) # define o valor da spin no slider
    
    # ChangedEvent (blue Slider)
    def changedSliderBlue(self):
        value = self.sliderBlue.value() # Obtem o valor que está no slider
        self.spinBlue.setValue(value) # define o valor da slider no spin
        self.rgbCODE()
        self.hexCODE()   
    
    # ChangedEvent (blue Spin)
    def changedSpinBlue(self):
        value = self.spinBlue.value() # Obtem o valor que está no spin
        self.sliderBlue.setValue(value) # define o valor da spin no slider

    # Organiza o RGB e exibe:
    def rgbCODE(self):
        valorRed = str(self.sliderRed.value())
        valorGreen = str(self.sliderGreen.value())
        valorBlue = str(self.sliderBlue.value())
        valorCompleto = "RGB ({}, {}, {})".format(valorRed, valorGreen, valorBlue)
        self.txtRGB.setText(valorCompleto)

    # Converte para Hexadecimal:
    def converteHex(self, decimal):
        return hex(decimal)[2:]
    
    # Coloca um zero a esquerda se necessario no valor hexadecimal:
    def zeroLeftHex(self, hex):
        if (len(hex) == 1):
            return "0{}".format(hex)
        return hex

    # Organiza o HEX e exibe:
    def hexCODE(self):
        valorRed = str(self.converteHex(self.sliderRed.value()))
        valorRed = self.zeroLeftHex(valorRed)
        valorGreen = str(self.converteHex(self.sliderGreen.value()))
        valorGreen = self.zeroLeftHex(valorGreen)
        valorBlue = str(self.converteHex(self.sliderBlue.value()))
        valorBlue = self.zeroLeftHex(valorBlue)
        valorCompleto = "#{}{}{}".format(valorRed, valorGreen, valorBlue)
        self.txtHEX.setText(valorCompleto)
        self.setColor(valorCompleto)

    # coloca a cor no quadrado:
    def setColor(self, hexColor):
        self.SelectedCor.setStyleSheet("background-color:{};".format(hexColor))
    
    # copia o código rgb:
    def copyRGB(self):
        self.txtRGB.selectAll()
        self.txtRGB.copy()
        self.txtRGB.deselect()
    
    # copia o código hex:
    def copyHEX(self):
        self.txtHEX.selectAll()
        self.txtHEX.copy()
        self.txtHEX.deselect()



# Inicialização
app = QApplication(sys.argv)
window = Janela()
sys.exit(app.exec())
