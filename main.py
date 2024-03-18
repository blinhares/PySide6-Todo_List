import sys
from src.py.todo_lib import Todo


from PySide6.QtCore import Qt
from src.mainwindowtodo import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)


class TodoList(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.setupUi(self)
        self.statusBar().showMessage('Seja Bem-Vindo',5000)
        self.setWindowTitle('ToDo - List. Organize-se!')
        self.nome = 'minhalista'

        self.nomeListaTarefas.setText(self.nome)
        self.lista_tarefas = Todo(self.nome)

        self._show_list()

        self.botDesfazer.clicked.connect(self._undone_last_action)
        self.botRecuperarTudo.clicked.connect(self._recovery_all)
        self.botApagarTudo.clicked.connect(self._on_press_apagar_tudo)
        self.botAdd.clicked.connect(self._on_press_add)

    def _make_slot(self,func,*args, **kargs):
        @Slot()
        def real_slot():
            func(*args,**kargs)
        return real_slot
    
    @Slot()
    def _erase_item_when_but_press(self, button_text:str):
        self.lista_tarefas.remove_by_id(int(button_text))
        self.lista_tarefas.save_file()
        self._clear_list()
        self._show_list()

    def _undone_last_action(self):
        if len(self.lista_tarefas._todo_list_trash)>0:
            self.lista_tarefas.recovery_last()
            self.lista_tarefas.save_file()
            self._clear_list()
            self._show_list()

    def _recovery_all(self):
        self.lista_tarefas.recovery_all()
        self.lista_tarefas.save_file()
        self._clear_list()
        self._show_list()

    def _conect_clicked_button_to_slot(self, button:QPushButton,slot):
        button.clicked.connect(slot)
    
    def _show_list(self): 
        '''
        Recebe uma lista proveniente da classe Todo no modelo abaixo e retorna somente as chaves task.
        ```
        [{'id': 0, 'task': 'Iniciar Projeto'}, {'id': 1, 'task': 'Finalizar Projeto'}]
        ```
        Resultado:
        ```
        ['Iniciar Projeto', 'Finalizar Projeto']
        ```
        '''
        #criar um layout horizontal
        
        list_=self.lista_tarefas.list_all() # TODO ordenar para que a lista seja impressa do ultiom para o primeiro
        lay_scrol_area = QVBoxLayout()
        #alinhando os itens ao topo
        lay_scrol_area.setAlignment(Qt.AlignmentFlag.AlignTop)
        for i in range(len(list_)):
            bot_texto = QPushButton(str(list_[i]['task'])) #TODO - adicionar comando de ediatar tarefa quando a linha for apertado
            lay_scrol_area_linha = QHBoxLayout()

            erase_button = QPushButton('X')
            erase_button.setObjectName(str(list_[i]['id']))
            erase_button.setMaximumWidth(40)
            slot = self._make_slot(self._erase_item_when_but_press,
                                   str(list_[i]['id']))
            self._conect_clicked_button_to_slot(erase_button, slot)
            
            lay_scrol_area_linha.addWidget(bot_texto)
            lay_scrol_area_linha.addWidget(erase_button)
            lay_scrol_area.addLayout(lay_scrol_area_linha)
        self.scrollAreWidContents.setLayout(lay_scrol_area) 

    def _clear_list(self):
        self.scrollAreWidContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreWidContents)

    def _on_press_apagar_tudo(self):
        self.lista_tarefas.remove_all()
        self._clear_list()

    def _on_press_add(self):
        if not self._is_field_empty():
            task = self._get_text_from_field()
            self._clear_text_from_field()
            self.lista_tarefas.add(task=task)
            self._clear_list()
            self._show_list()


    def _is_field_empty(self) -> bool:
        if len(self.lineEdit.text()) < 1:
            return True
        return False
    
    def _get_text_from_field(self) -> str:
        return self.lineEdit.text()
    
    def _clear_text_from_field(self):
        self.lineEdit.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = TodoList()
    main_window.show()

    app.exec()

    
    