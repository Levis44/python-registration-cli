import menus

id_accumulator = 0

class Client():
  def __init__(self, name, birth, phone, email):
    global id_accumulator
    id_accumulator += 1

    self.client_id = id_accumulator
    self.name = name
    self.birth = birth
    self.phone = phone
    self.email = email
    self.categories = []
  
  def categoryQuestions(self, category):
    if category == 4:
      client_cpf, client_rg, client_family_income = menus.atendidosMenu()
      
      self.client_cpf = client_cpf
      self.client_rg = client_rg
      self.client_family_income = client_family_income

    if category == 5:
      client_visitor_name, client_visitor_phone, client_visitor_rg = menus.visitantesMenu()

      self.client_visitor_name = client_visitor_name
      self.client_visitor_phone = client_visitor_phone
      self.client_visitor_rg = client_visitor_rg

