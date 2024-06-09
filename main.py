#Task_1,2
import requests


class Rate:
    def __init__(self, diff=False, currency_format='value'):
        self.diff = diff
        self.format = currency_format
        self.currencies = self.get_currencies()

    def get_currencies(self):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url).json()
        currencies = response['Valute']
        return currencies

    def get_currency_with_max_rate(self):
        max_rate_currency = max(self.currencies.values(), key=lambda x: x['Value'])
        return max_rate_currency['Name']

    def make_format(self, currency):
        if currency in self.currencies:
            if self.format == 'full':
                return self.currencies[currency]

            if self.format == 'value':
                return self.currencies[currency]['Value']

        return 'Error'

    def eur(self):
      if self.diff == True:
        return abs(self.currencies['EUR']['Value'] - self.currencies['EUR']['Previous'])
      else:
        # """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')

    def usd(self):
      if self.diff == True:
        return abs(self.currencies['USD']['Value'] - self.currencies['USD']['Previous'])
      else:
        # """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

    def brl(self):
      if self.diff == True:
        return abs(self.currencies['BRL']['Value'] - self.currencies['BRL']['Previous'])
      else:
        # """Возвращает курс бразильского реала на сегодня в формате self.format"""
        return self.make_format('BRL')



print(Rate(currency_format="full", diff=True).brl())

#Task_3
class Employee:
  def __init__(self, name, seniority):
    self.name = name
    self.seniority = seniority
    self.grade = 2

  def grade_up(self):
    """Повышает уровень сотрудника"""
    self.grade += 1

  def publish_grade(self):
    """Публикация результатов аккредитации сотрудников"""
    print(self.name, self.grade)

  def check_if_it_is_time_for_upgrade(self):
    pass

class Designer(Employee):
  def __init__(self, name, seniority):
    super().__init__(name, seniority)


  def check_if_it_is_time_for_upgrade(self):
    self.seniority += 1

    if self.seniority % 7 == 0:
      self.grade_up()

    return self.publish_grade()

  def receive_award(self):
    self.seniority += 2