import sys
from PyQt5.QtWidgets import QApplication

from initializations import init_create_db
from menu import Menu


def application():
    app = QApplication(sys.argv)
    m = Menu()
    m.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    # init_create_db()
    application()

# if __name__ == "__main__":
#     password = random_password()
#     print(password)
#     print(len(password))
