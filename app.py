import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QMenu

# инстанс приложения
# на одно приложение строго один инстанс
app = QApplication(sys.argv)

# первое окно, которые мы писали сами
# это главное окно, в котором мы можем размещать вообще всё, что нужно для приложения
# если сравнивать с html-документом, то это тег <body> (а QApplication - <html>)
class MainWindow(QMainWindow):
    # метод инициализации
    def __init__(self):
        # вызываем родительский метод
        super().__init__()

        # храним в окне значение, было ли переключено или нет
        self.is_toggled = True
        self.button_is_checked = True

        # определяем заголовок окна, которое открывается при запуске
        self.setWindowTitle("Hello!")

        # создаем кнопку
        self.button = QPushButton("Press F")
        # делаем так, чтобы можно ее было "выбирать" (как <input type="checkbox">)
        self.button.setCheckable(True)

        # определяем размер окна
        self.setFixedSize(QSize(400, 300))

        # добавляем кнопку в наше окно
        self.setCentralWidget(self.button)

        # отлавливаем событие, когда кнопка нажимается и выполняем метод button_was_clicked()
        self.button.clicked.connect(self.button_was_clicked)

        # то же самое, только проверяем, была ли кнопка переключена или отпущена (кнопкой мыши)
        # self.button.clicked.connect(self.button_was_toggled)
        # self.button.clicked.connect(self.button_was_released)

    # методы для обработки событий
    def button_was_clicked(self):
        # меняем текст кнопки
        self.button.setText("Вы уже нажали на кнопку")
        # делаем ее некликабельной (<button disabled></button>)
        self.button.setEnabled(False)
        print('Clicked')

    def button_was_toggled(self, checked):
        # сохраняем в нашу переменную состояние кнопки
        self.is_toggled = checked
        print('Checked?', self.is_toggled)

    def button_was_released(self):
        # сохраняем в нашу переменную состояние кнопки (уже из самой кнокпи, а не события)
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

# второе окно
class SecondMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # сетим новый заголовок
        self.setWindowTitle("Hello!")

        # создаем новый <label> и <input>
        self.label = QLabel()
        self.input = QLineEdit()

        # при событии изменения значения в input, сетим в label то, что написать в input
        self.input.textChanged.connect(self.label.setText)

        self.setFixedSize(QSize(400, 300))

        # создаем макет приложения и добавляем туда инпут и лэйбл
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        # создаем контейнер (<div>) и добавляем туда наш макет с элементами
        container = QWidget()
        container.setLayout(layout)

        # добавляем контейнер в окно
        self.setCentralWidget(container)


# третье окно
class ThirdMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # добавляем новый лэйбл
        self.label = QLabel("Press me")
        # сразу добавляем его в окно
        self.setCentralWidget(self.label)
        self.setFixedSize(QSize(400, 300))

    # метод, который срабатывает при событии, а именно на нажатии мыши
    def mousePressEvent(self, e):
        # если нажимаем на левую клавишу, выходит соответствующее сообщение, если на правую, то аналогично
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")


# четвертое окно
class FourthMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    # добавляем метод, который создает контекстное меню (которое открывается нажатием правой мыши)
    def contextMenuEvent(self, e):
        # создаем само меню
        context = QMenu(self)

        # добавляем варианты
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))

        # запускаем и передаем позицию, где оно должно открыться (опеределяется по месту нажатия правой клавиши мыши)
        context.exec(e.globalPos())


# создаем инстанс окна
window = ThirdMainWindow()
# показываем его
window.show()

# запускаем приложение
app.exec()
