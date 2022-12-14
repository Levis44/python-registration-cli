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
    if category == 1:
      client_salary, client_work_hours, client_payment_day = menus.employeesMenu()

      self.client_salary = client_salary
      self.client_work_hours = client_work_hours
      self.client_payment_day = client_payment_day

    if category == 2:
      client_available_day, client_available_hour, client_second_phone = menus.volunteersMenu()

      self.client_available_day = client_available_day
      self.client_available_hour = client_available_hour
      self.client_second_phone = client_second_phone

    if category == 3:
      client_donation_amount, client_recursive_donation, client_project_donation = menus.donorsMenu()
      
      self.client_donation_amount = client_donation_amount
      self.client_recursive_donation = client_recursive_donation
      self.client_project_donation = client_project_donation

    if category == 4:
      client_cpf, client_rg, client_family_income = menus.treatedsMenu()

      self.client_cpf = client_cpf
      self.client_rg = client_rg
      self.client_family_income = client_family_income

    if category == 5:
      client_visitor_name, client_visitor_phone, client_visitor_rg = menus.visitorsMenu()

      self.client_visitor_name = client_visitor_name
      self.client_visitor_phone = client_visitor_phone
      self.client_visitor_rg = client_visitor_rg

