from atracacao import Atracacao
from carga import Carga

class Antaq:
  
  def __init__(self, year=2017, month=1):
    self.year = year
    self.month = month
    
  def return_atracao(self):
    atracacao = Atracacao(year=self.year)
    return atracacao.return_data()
  
  def return_carga(self):
    carga = Carga(year=self.year)
    return carga.return_data()
    
