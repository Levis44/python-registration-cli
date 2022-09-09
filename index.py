

clients = []
id_accumulator = 0

class Client():
  def __init__(self, client_id, name, birth, phone, email):
    self.client_id = client_id
    self.name = name
    self.birth = birth
    self.phone = phone
    self.email = email
    self.categories = []
  def print_self(self, arr):
    properties = []

    for attr in arr:
      value = "%s: %r" % (attr, getattr(self, attr))
      properties.append(value)

    print(properties)

def menu():
  possible_inputs = [1, 2, 3, 4]  

  option = int(input('''
Escolha uma das opções abaixo:

[1] - Cadastrar um novo Cliente
[2] - Consultar um cliente pelo id
[3] - Sair do programa

'''))

  res = option in possible_inputs

  if not res:
    print('''
Escolha inválida, digite uma opção válida
----------------------------------------------------------''')
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
----------------------------------------------------------

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

def print_category_att(client, category):
  if category == 1:
    print("Nada")
  if category == 2:
    print("Nada")
  if category == 3:
    print("Nada")
  if category == 4:
    print("CPF: ", client.cpf)
    print("RG: ", client.rg)
    print("Renda familiar: ", client.family_income)
  if category == 5:
    print("Nada")

def choose_category_string(category):
  switcher = {
        1:'Funcionários',
        2:'Voluntários',
        3:'Doadores',
        4:'Atendidos',
        5:'Visitantes',
    }

  return switcher.get(category)

def category_questions(category, client):
  if category == 4:
      return atendidos_questions(client)

def atendidos_questions(client):
  client_cpf = input('Digite o CPF do cliente: ')
  client_rg = input('Digite o RG do cliente: ')
  client_family_income = input('Digite a renda familiar do cliente: ')

  setattr(client, "cpf", client_cpf)
  setattr(client, "rg", client_rg)
  setattr(client, "family_income", client_family_income)

def register_client():
  client_id, client_name, client_birth, client_phone, client_email = init_register()

  client = Client(client_id, client_name, client_birth, client_phone, client_email)
  
  #  Escolher a categoria
  category = category_menu(client)
  
  clients.append(client)

  print("----------------------------------------------------------")
  print("")
  print("")
  print("")

  print("Id: ", client.client_id)
  print("Nome: ", client.name)
  print("Data de Nascimento: ", client.birth)
  print("Telefone: ", client.phone)
  print("Email: ", client.email)

  print_category_att(client, category)

  print(clients)
  print('Cliente adicionado com sucesso')


def start(): 
  while True:
    option = menu()

    if option == 1 :
      register_client()
    if option == 2 :
      print("Salveee1")
    if option == 3 :
      break

start()