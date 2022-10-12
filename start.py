import menus
import handlers

def start(): 
  while True:
    option = menus.initialMenu()

    if option == 1:
      handlers.handleRegister()
    if option == 2:
      print("Salveee2")
    if option == 3:
      break

start()