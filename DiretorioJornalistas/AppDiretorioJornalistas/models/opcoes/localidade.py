import requests


def Estados():
  estados = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados')
  estados = estados.json()
  lista_estados = []
  for estado in estados:
    lista_estados.append((estado['id'],estado['nome'] +', '+ estado['sigla']))
  return lista_estados


def Cidades():
    # url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + uf + '/municipios'
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
    cidades = requests.get(url).json()
    lista_cidades = []
    for cidade in cidades:
      lista_cidades.append((cidade['id'], cidade['nome']+ ', ' + cidade['microrregiao']['mesorregiao']['UF']['sigla']))
    return lista_cidades

