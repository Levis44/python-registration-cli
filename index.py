

clients = []
id_accumulator = 0

class Client():
  def init_register(self, client_id, name, birth, phone, email):
    self.client_id = client_id
    self.name = name
    self.birth = birth
    self.phone = phone
    self.email = email

  def print_self(self, arr):
    properties = []

    for attr in arr:
      value = "%s: %r" % (attr, getattr(self, attr))
      properties.append(value)

    print(properties)


def menu():
  possible_inputs = [1, 2, 3, 4]  

  option = int(input('''
Para iniciar o sistema, escolha uma das opções abaixo:

[1] - Cadastrar cliente
[2] - Consultar Clientes
[3] - Editar Cliente
[4] - Sair do programa

'''))

  res = option in possible_inputs

  if not res:
    print("Escolha inválida, digite uma opção válida")
    menu()

  return option

   
def init_register():
  global id_accumulator
  id_accumulator += 1
  client_id = id_accumulator
  client_name = input('Digite o nome do cliente: ')
  client_birth = input('Digite a data de nascimento do cliente: ')
  client_phone = input('Digite o telefone do cliente: ')
  client_email = input('Digite o email do cliente: ')
  
  return (client_id, client_name, client_birth, client_phone, client_email)

def category_menu(client):
  #  Escolher a categoria
  category = choose_category()
  client_category_string = choose_category_string(category)
  client.categories.append(client_category_string)
  category_questions(category, client)
  return category

def choose_category(): 
  possible_inputs = [1, 2, 3, 4, 5]  
  category = int(input('''
Escolha a categoria do novo cliente

[1] - Funcionários
[2] - Voluntários
[3] - Doadores
[4] - Atendidos
[5] - Visitantes

'''))

  res = category in possible_inputs

  if not res:
    print("Escolha inválida, digite uma opção válida")
    choose_category()

  return category
  
def choose_category_string(category):
  switcher = {
        1:'Funcionários',
        2:'Voluntários',
        3:'Doadores',
        4:'Atendidos',
        5:'Visitantes',
    }

  return switcher.get(category)

def category_questions(category):
  if category == 4:
      return atendidos_questions()

def atendidos_questions():
  client_cpf = input('Digite o CPF do cliente: ')
  client_rg = input('Digite o RG do cliente: ')
  client_family_income = input('Digite a renda familiar do cliente: ')

  return (client_cpf, client_rg, client_family_income)

def register_client():

  client_id, client_name, client_birth, client_phone, client_email = init_register()
  
  client = {
    "id": client_id,
    "client_name": client_name
  }

  setattr(client, "test", 1)

  clients.append(client)
  
  # # Escolher a categoria
  # category = choose_category()

  # client_category = choose_category_string(category)
  
  
  # # clients.append(client_data)

  # print(getattr(clients[0], "aaa"))

  print(clients)
  print('Cliente adicionado com sucesso')


def start(): 
  while True:
    option = menu()

    if option == 1 :
      register_client()
    if option == 2 :
      print("Salveee2")
    if option == 4 :
      break

start()