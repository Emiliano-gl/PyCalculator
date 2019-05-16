import sys
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    calculator.show()
    sys.exit(app.exec_())
