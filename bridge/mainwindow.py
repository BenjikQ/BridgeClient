import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from .ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self: "MainWindow") -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # type: ignore[no-untyped-call]


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
