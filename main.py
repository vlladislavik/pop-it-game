from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import sys
import random
import json

class PopItGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pop_it_game.ui', self)
        self.active_style = 'background-color: rgb(0, 85, 255); border: 3px solid black; border-radius: 75px;'
        self.passive_style = 'background-color: rgb(255, 255, 255); border: 3px solid black; border-radius: 75px;'
        self.all_rnds = [self.rnd_0, self.rnd_1, self.rnd_2, self.rnd_3, self.rnd_4,
                         self.rnd_5, self.rnd_6, self.rnd_7, self.rnd_8, self.rnd_9]
        self.active_round = random.choice(self.all_rnds)
        self.active_round.setStyleSheet(self.active_style)
        self.result_count = 0

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0:
            self.rnd_0.setStyleSheet(self.passive_style)
        if event.key() == Qt.Key_1:
            self.rnd_1.setStyleSheet(self.passive_style)
        if event.key() == Qt.Key_2:
            self.rnd_2.setStyleSheet(self.passive_style)
        if event.key() == Qt.Key_3:
            self.rnd_3.setStyleSheet(self.passive_style)
        if event.key() == Qt.Key_4:
            self.rnd_4.setStyleSheet(self.passive_style)
        if event.key() == Qt.Key_5:
            self.rnd_5.setStyleSheet(self.passive_style)
        if event.key() == Qt.Key_6:
            self.rnd_6.setStyleSheet(self.passive_style)
        if event.key() == Qt.Key_7:
            self.rnd_7.setStyleSheet(self.passive_style)
        if event.key() == Qt.Key_8:
            self.rnd_8.setStyleSheet(self.passive_style)
        if event.key() == Qt.Key_9:
            self.rnd_9.setStyleSheet(self.passive_style)

        if (event.key() - 48) == self.all_rnds.index(self.active_round):
            self.result_count += 1
            self.result.setText(f'Результат: {str(self.result_count)}')
        else:
            with open('results.json', 'r') as file:
                data = json.load(file)
                data['results'].append(self.result_count)

            with open('results.json', 'w') as file:
                json.dump(data, file)
            return self.result_count

        self.active_round = random.choice(self.all_rnds)
        self.active_round.setStyleSheet(self.active_style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PopItGame()
    ex.show()
    sys.exit(app.exec_())
