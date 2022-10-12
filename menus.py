
def initialMenu():
  option = int(input('''
Escolha uma das opções abaixo:

[1] - Cadastrar um novo Cliente
[2] - Consultar um cliente pelo id
[3] - Sair do programa

'''))

  return option

def initClientRegistration():
  client_name = input('Digite o nome do cliente: ')
  client_birth = input('Digite a data de nascimento do cliente: ')
  client_phone = input('Digite o telefone do cliente: ')
  client_email = input('Digite o email do cliente: ')
  
  return (client_name, client_birth, client_phone, client_email)
  

def categoryMenu():
  category = int(input('''
----------------------------------------------------------

Escolha a categoria do novo cliente

[1] - Funcionários
[2] - Voluntários
[3] - Doadores
[4] - Atendidos
[5] - Visitantes

'''))

  return category

def atendidosMenu():
  client_cpf = input('Digite o CPF do cliente: ')
  client_rg = input('Digite o RG do cliente: ')
  client_family_income = input('Digite a renda familiar do cliente: ')

  return (client_cpf, client_rg, client_family_income)

def visitantesMenu():
  client_visitor_name = input('Digite o nome de quem o cliente irá visitar: ')
  client_visitor_phone = input('Digite o telefone de quem o cliente irá visitar: ')
  client_visitor_rg = input('Digite o rg da pessoa que o cliente irá visitar: ')

  return (client_visitor_name, client_visitor_phone, client_visitor_rg)

