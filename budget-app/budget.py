class Category:
      

  def __init__(self, category):
    self.category = category
    self.ledger = []


  def __str__(self):
    string_answer = self.category.center(30, "*") + "\n"

    for item in self.ledger:
      temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      string_answer += temp + "\n"

    string_answer += "Total: " + str(self.get_balance())
    return string_answer

  def deposit(self, amount, description=""):
    temp = {}
    temp['amount'] = amount
    temp['description'] = description
    self.ledger.append(temp)


  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      temp = {}
      temp['amount'] = 0 - amount
      temp['description'] = description
      self.ledger.append(temp)
      return True
    return False


  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return balance


  def transfer(self, amount, budget_cat):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget_cat.category)
      budget_cat.deposit(amount, "Transfer from " + self.category)
      return True
    return False


  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True


def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += (item['amount'])
    spend.append(temp)
  
  total_spend = sum(spend)
  per = [h/total_spend * 100 for h in spend]

  string_answer = "Percentage spent by category"
  for h in range(100, -1, -10):
    string_answer += "\n" + str(h).rjust(3) + "|"
    for c in per:
      if c > h:
        string_answer += " o "
      else:
        string_answer += "   "
    # Spaces
    string_answer += " "
  string_answer += "\n    ----------"

  categoty_len = []
  for category in categories:
    categoty_len.append(len(category.category))
  max_length = max(categoty_len)

  for h in range(max_length):
    string_answer += "\n    "
    for c in range(len(categories)):
      if h < categoty_len[c]:
        string_answer += " " + categories[c].category[h] + " "
      else:
        string_answer += "   "
    # Spaces
    string_answer += " "

  return string_answer
