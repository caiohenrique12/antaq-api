import urllib.request
import os, errno
import zipfile as zp
import pandas as pd

class Extract:
  
  def __init__(self, year=2017, type_file=''):
    self.year = year
    self.type_file = type_file
  
  def final_data(self):
    self.extract_file()
    return self.to_pandas()
    
  def to_pandas(self):
    df = pd.read_csv(f'{os.getcwd()}/csv_data/{self.year}{self.type_file}_extract/{self.year}{self.type_file}.txt', sep=';')
    df = self.clean_df(df)
    
    # eu sei que tem maneira melhor de fazer
    if self.type_file == 'Atracacao':
      df = df[['IDAtracacao', 'CDTUP', 'IDBerco',
              'Berço', 'Porto Atracação', 'Apelido Instalação Portuária',
              'Complexo Portuário', 'Tipo da Autoridade Portuária', 'Data Atracação',
              'Data Chegada', 'Data Desatracação', 'Data Início Operação',
              'Data Término Operação', 'Ano', 'Mes', 'Tipo de Operação']]
    elif self.type_file == 'Carga':
      df = df[['IDCarga', 'IDAtracacao', 'Origem',
              'Destino', 'CDMercadoria', 'Tipo Operação da Carga',
              'Carga Geral Acondicionamento', 'ConteinerEstado',
              'Tipo Navegação', 'FlagAutorizacao', 'FlagCabotagem',
              'FlagCabotagemMovimentacao', 'FlagConteinerTamanho',
              'FlagLongoCurso', 'FlagMCOperacaoCarga', 'FlagOffshore']]
    return df[:100].reset_index().to_dict('records')
    
  def clean_df(self, df):
    df = df.dropna()
    return df
    
  def extract_file(self):
    self.download_file()
    with zp.ZipFile(f'{os.getcwd()}/csv_data/{self.year}{self.type_file}.zip', 'r') as zip_ref:
      zip_ref.extractall(f'{os.getcwd()}/csv_data/{self.year}{self.type_file}_extract')
      print(f'unzip {self.year} was successful.')
      os.remove(f'{os.getcwd()}/csv_data/{self.year}{self.type_file}.zip')
    
  def download_file(self):
    self.create_folder()
    if not os.path.exists(f'{os.getcwd()}/csv_data/{self.year}{self.type_file}.zip'):
      url = f'http://web.antaq.gov.br/Sistemas/ArquivosAnuario/Arquivos/{self.year}{self.type_file}.zip'
      urllib.request.urlretrieve(url, f'{os.getcwd()}/csv_data/{self.year}{self.type_file}.zip')
      print(f'Downloading for {self.year} was complete with success.')

  def create_folder(self):
    try:
      os.makedirs(f'{os.getcwd()}/csv_data/')
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise
