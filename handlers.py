from client import Client
import menus

clients = []

def handleRegister():
  # pick first info
  client_name, client_birth, client_phone, client_email = menus.initClientRegistration()

  # create client
  client = Client(client_name, client_birth, client_phone, client_email)

  # choose category
  category = menus.categoryMenu()

  # add category to client
  client.categories.append(category)

  # add attributes from category
  client.categoryQuestions(category)

  # add client to fake database
  clients.append(client)

  print(vars(client))

def findClientById():
  id = menus.getClientId()

  for client in clients:
    print(client.client_id)
    print(id)
    if client.client_id == id:
      print(vars(client))
    else:
       print("Nenhum cliente com o id")

 
