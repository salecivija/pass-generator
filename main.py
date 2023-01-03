import random
import string

from PyQt5 import QtWidgets

class PasswordGenerator(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    # Set up the user interface
    self.initUI()

  def initUI(self):
    # Create a button for generating passwords
    self.btn = QtWidgets.QPushButton("Generate password", self)
    self.btn.clicked.connect(self.generate_password)

    # Create a text field for displaying the generated password
    self.password_field = QtWidgets.QLineEdit(self)
    self.password_field.setReadOnly(True)

    # Create a layout and add the button and text field to it
    layout = QtWidgets.QVBoxLayout(self)
    layout.addWidget(self.btn)
    layout.addWidget(self.password_field)

    # Set the window title and show the widget
    self.setWindowTitle("Password Generator")
    self.show()

  def generate_password(self):
    # Create a list of characters to choose from
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Select 4 small letters at random
    password = random.choices(string.ascii_lowercase, k=4)
    
    # Select 4 numbers at random
    password += random.choices(string.digits, k=4)

    # Select 3 capital letters at random
    password += random.choices(string.ascii_uppercase, k=3)

    # Convert the list of characters into a string and display it in the text field
    self.password_field.setText("".join(password))

if __name__ == "__main__":
  app = QtWidgets.QApplication([])
  generator = PasswordGenerator()
  app.exec_()


