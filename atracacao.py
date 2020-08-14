from extract import Extract

class Atracacao:
  
  def __init__(self, year=2017, month=1):
    self.year = year
    self.month = month
    
  def return_data(self):
    extract = Extract(year=self.year, type_file='Atracacao')
    return extract.final_data()
