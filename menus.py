
def initialMenu():
  option = int(input('''
Escolha uma das opções abaixo:

[1] - Cadastrar um novo Cliente
[2] - Consultar um cliente pelo id
[3] - Sair do programa

'''))

  return option

def getClientId():
  id = int(input('''
Digite o id do cliente que deseja buscar:

'''))
  return id

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

def employeesMenu():
  client_salary = input('Digite o salário do empregado: ')
  client_work_hours = input('Digite quantas horas o empregado irá trabalhar: ')
  client_payment_day = input('Digite o dia do pagamento do empregado: ')

  return (client_salary, client_work_hours, client_payment_day)

def volunteersMenu():
  client_available_day = input('Digite o dia da semana que você estaria disponível para participar de eventos: ')
  client_available_hour = input('Digite o melhor horário que você poderia participar: ')
  client_second_phone = input('Digite um outro telefone para contato: ')

  return (client_available_day, client_available_hour, client_second_phone)

def donorsMenu():
  client_donation_amount = input('Digite a quantia de dinheiro que o cliente irá doar: ')
  client_recursive_donation = input('O cliente irá doar todos os meses? (SIM ou NÂO): ')
  client_project_donation = input('Digite o projeto que o cliente irá doar: ')

  return (client_donation_amount, client_recursive_donation, client_project_donation)

def treatedsMenu():
  client_cpf = input('Digite o CPF do cliente: ')
  client_rg = input('Digite o RG do cliente: ')
  client_family_income = input('Digite a renda familiar do cliente: ')

  return (client_cpf, client_rg, client_family_income)

def visitorsMenu():
  client_visitor_name = input('Digite o nome de quem o cliente irá visitar: ')
  client_visitor_phone = input('Digite o telefone de quem o cliente irá visitar: ')
  client_visitor_rg = input('Digite o rg da pessoa que o cliente irá visitar: ')

  return (client_visitor_name, client_visitor_phone, client_visitor_rg)

